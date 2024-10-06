from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_date', 'slug']
    list_filter = ['publishing_date']
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)
