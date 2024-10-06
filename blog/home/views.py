from django.shortcuts import render
from django.contrib.auth.models import User
from post.models import Post

def home_view(request):
    most_viewed_posts = Post.objects.order_by('-views_count')[:5]
    total_users = User.objects.count()
    total_post_writers = Post.objects.values('user').distinct().count()
    total_post_readers = sum(post.views_count for post in Post.objects.all())
    
    context = {
        'most_viewed_posts': most_viewed_posts,
        'total_users': total_users,
        'total_post_writers': total_post_writers,
        'total_post_readers': total_post_readers,
    }
    return render(request, 'home.html', context)
