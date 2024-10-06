
from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    
    path('index/', views.post_index,name='index'),
    path('create/',views.post_create,name='create'),
    path('<slug:slug>/', views.post_detail,name='detail'),# arama motorunda ip/post/id(rakam olacak) girildiğinde girilen id' ye ait postun detay sayfasına gider cunku her post primary key olarak id alıyor
   
    path('<slug:slug>/update/',views.post_update,name='update'),
    path('<slug:slug>/delete/',views.post_delete,name='delete'),

]
