from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import SearchFilter

from .models import Post, PostImage
from .serializers import PostSerializer, PostImageSerializer


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [SearchFilter]

    search_fields = [
        'title',
        'content',
        'author__username'
    ]


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
    

class PublishedPostListView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(
            status='published'
        )

class PostImageUploadView(CreateAPIView):
    serializer_class = PostImageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        post_id = self.kwargs['post_id']

        post = Post.objects.get(id=post_id)

        if post.author != self.request.user:
            raise PermissionDenied(
                "You are not allowed to upload images to this post"
            )

        serializer.save(post=post)