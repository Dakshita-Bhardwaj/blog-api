from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import Post
from .serializers import PostSerializer
from rest_framework import status

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):

    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save(author=request.user)

        return Response(serializer.data)

    return Response(serializer.errors)

@api_view(['GET'])
def get_posts(request):

    posts = Post.objects.all()

    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_post(request, post_id):

    try:
        post = Post.objects.get(id=post_id)

    except Post.DoesNotExist:
        return Response(
            {"error": "Post not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if post.author != request.user:
        return Response(
            {"error": "You are not allowed to edit this post"},
            status=status.HTTP_403_FORBIDDEN
        )

    serializer = PostSerializer(
        post,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, post_id):

    try:
        post = Post.objects.get(id=post_id)

    except Post.DoesNotExist:
        return Response(
            {"error": "Post not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if post.author != request.user:
        return Response(
            {"error": "You are not allowed to delete this post"},
            status=status.HTTP_403_FORBIDDEN
        )

    post.delete()

    return Response(
        {"message": "Post deleted successfully"}
    )

@api_view(['GET'])
def get_post(request, post_id):

    try:
        post = Post.objects.get(id=post_id)

    except Post.DoesNotExist:
        return Response(
            {"error": "Post not found"},
            status=404
        )

    serializer = PostSerializer(post)

    return Response(serializer.data)