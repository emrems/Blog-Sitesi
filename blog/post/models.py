from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    #id = models.AutoField(primary_key=True) bu kısmı olusturmaya gerek yok django zaten default olarak id'yi primary key olarak atıyor
    user = models.ForeignKey('auth.User', verbose_name='yazar', related_name='posts', on_delete=models.CASCADE)

    title=models.CharField(max_length=120,verbose_name='Başlık')
    content=models.TextField(verbose_name='içerik')
    publishing_date=models.DateTimeField(verbose_name='Yayınlanma tarihi',auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def increase_views(self):
       self.views_count += 1
       self.save()


    def get_absolute_url(self):
        return reverse('post:detail', args=[str(self.slug)])
    
    def get_create_url(self):
        return reverse('post:create')
    
    def get_update_url(self):
        return reverse('post:update', args=[str(self.slug)])
    
    def get_delete_url(self):
        return reverse('post:delete', args=[str(self.slug)])
    
    # bu fonksiyonda eşsiz slugları bulur
    def get_unique_slug(self):
        slug=slugify(self.title.replace('ı','i'))
        unique_slug=slug
        counter=1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug='{}-{}'.format(slug,counter)
            counter+=1
        return unique_slug 


    
    def save(self,*args,**kwargs):
       
        self.slug = self.get_unique_slug()
        return super(Post,self).save(*args,**kwargs)
    

    class Meta:
        ordering=['-publishing_date']   

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    name=models.CharField(max_length=200,verbose_name="isim")
    content=models.TextField(verbose_name='yorum')
    created_date=models.DateTimeField(auto_now_add=True)
    

