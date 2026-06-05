from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

class Post(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    title = models.CharField(max_length=200)
    
    content = models.TextField()

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ]
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
        )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    published_at = models.DateTimeField(
    null=True,
    blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class PostImage(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(
        upload_to='post_images/'
    )

    def __str__(self):
        return f"Image for {self.post.title}"