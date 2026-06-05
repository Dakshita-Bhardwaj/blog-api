from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostImageUploadView
)

urlpatterns = [
    path('', PostListView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('<uuid:post_id>/', PostDetailView.as_view()),
    path('<uuid:post_id>/update/', PostUpdateView.as_view()),
    path('<uuid:post_id>/delete/', PostDeleteView.as_view()),
    path('<uuid:post_id>/images/upload/', PostImageUploadView.as_view()),
]