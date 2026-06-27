from rest_framework import serializers
from .models import Post, PostImage


class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = [
            'uid',
            'image'
        ]


class PostSerializer(serializers.ModelSerializer):

    author = serializers.CharField(
        source='author.username',
        read_only=True
    )

    images = PostImageSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Post
        fields = [
            'uid',
            'title',
            'content',
            'author',
            'status',
            'published_at',
            'images',
            'created_at',
            'updated_at'
        ]

        read_only_fields = [
            'author',
            'created_at',
            'updated_at'
        ]