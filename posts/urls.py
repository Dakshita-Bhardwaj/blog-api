from django.urls import path
from .views import (
    create_post,
    get_posts,
    update_post,
    delete_post,
    get_post
)

urlpatterns = [
    path('', get_posts),
    
    path('create/', create_post),

    path('<int:post_id>/', get_post),

    path('<int:post_id>/update/', update_post),

    path('<int:post_id>/delete/', delete_post),
]