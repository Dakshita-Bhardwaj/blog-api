from django.contrib import admin
from .models import Post, PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'author',
        'published_at',
        'created_at',
        'updated_at'
    )

    search_fields = (
        'title',
        'content',
        'author__username'
    )
    
    list_filter = (
        'author',
        'created_at',
        'updated_at'
    )
    
    ordering = (
        '-created_at',
    )

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'post',
        'image'
    )

    search_fields = (
        'post__title',
    )