from django.shortcuts import render,HttpResponse, get_object_or_404,HttpResponseRedirect,redirect,Http404
from django.http import HttpResponseNotFound
from . models import Post
from .forms import PostForm,CommentForm
from django.contrib import messages
from django.utils.text import slugify
from django.db.models import Q

def post_index(request):
    post_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(title__icontains=query)
    return render(request, 'post/index.html', {'postk': post_list})#en sağdaki posts veritabanımızdan gelenler tırnak içine yazılan posts templatede for  içinde kullanılacak




def post_detail(request, slug):
    post=get_object_or_404(Post, slug=slug)
    post.views_count += 1
    post.save()
    
    form=CommentForm(request.POST or None  )

    if form.is_valid():
        comment=form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context={
        'post':post,
        'form':form
    }
    return render(request,'post/detail.html',context)





def post_create(request):
    #form = PostForm()#form nesnesi urettim
    if not request.user.is_authenticated:  
        return HttpResponseNotFound

    form=PostForm(request.POST or None , request.FILES or None )

    if form.is_valid():
        post=form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request,'başarılı bir şekilde oluşturuldu')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request,'post/form.html',context)






def post_update(request,slug):
    if not request.user.is_authenticated: 
        return HttpResponseNotFound()
    
    post = get_object_or_404(Post, slug=slug)

    form=PostForm(request.POST or None, request.FILES or None , instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'başarılı bir şekilde güncellendi')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }

    return render(request,'post/form.html',context)







def post_delete(request,slug):
    if not request.user.is_authenticated:  #kullanici giriş yapmış ise
        return HttpResponseNotFound()
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post:index')



