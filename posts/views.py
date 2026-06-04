from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import Post
from .serializers import PostSerializer


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'


class PostCreateView(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'

    def get_object(self):
        post = super().get_object()

        if post.author != self.request.user:
            raise PermissionDenied(
                "You are not allowed to edit this post"
            )

        return post
    
    


class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'

    def get_object(self):
        post = super().get_object()

        if post.author != self.request.user:
            raise PermissionDenied(
                "You are not allowed to delete this post"
            )

        return post