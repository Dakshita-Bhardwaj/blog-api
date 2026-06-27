from django.contrib import admin
from .models import Post, PostImage

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    inlines = [PostImageInline]

    list_display = (
        'uid',
        'title',
        'author',
        'status',
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
        'status',
        'author',
        'created_at',
        'updated_at'
    )
    
    ordering = (
        '-created_at',
    )

