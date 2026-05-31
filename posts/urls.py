from django.urls import path
from .views import create_post, get_posts, update_post, delete_post

urlpatterns = [
    path('', get_posts),
    path('create/', create_post),
    path('<int:post_id>/', update_post),
    path('delete/<int:post_id>/', delete_post),
]