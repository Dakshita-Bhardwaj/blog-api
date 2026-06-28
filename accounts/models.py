from datetime import timedelta

from django.db import models
from django.utils import timezone


class EmailOTP(models.Model):

    email = models.EmailField(
        unique=True
    )

    otp = models.CharField(
        max_length=6
    )

    is_verified = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def is_expired(self):
        return timezone.now() > self.updated_at + timedelta(minutes=5)

    def __str__(self):
        return self.email