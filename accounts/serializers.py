import random

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from rest_framework import serializers

from .models import EmailOTP

User = get_user_model()


class SendOTPSerializer(serializers.Serializer):

    email = serializers.EmailField()

    def create(self, validated_data):

        email = validated_data["email"]

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "An account with this email already exists."
            )

        otp_obj = EmailOTP.objects.filter(email=email).first()

        if otp_obj:
            seconds = (timezone.now() - otp_obj.created_at).total_seconds()

            if seconds < 60:
                remaining = int(60 - seconds)

                raise serializers.ValidationError(
                    f"Please wait {remaining} seconds before requesting another OTP."
                )

        otp = str(random.randint(100000, 999999))

        otp_obj, _ = EmailOTP.objects.update_or_create(
            email=email,
            defaults={
                "otp": otp,
                "is_verified": False,
            }
        )

        send_mail(
            subject="Your Verification Code",
            message=f"Your OTP is {otp}. It is valid for 5 minutes.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        return otp_obj


class VerifyOTPSerializer(serializers.Serializer):

    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, attrs):

        email = attrs["email"]
        otp = attrs["otp"]

        try:
            otp_obj = EmailOTP.objects.get(email=email)

        except EmailOTP.DoesNotExist:
            raise serializers.ValidationError(
                "OTP not found."
            )

        if otp_obj.is_expired():
            raise serializers.ValidationError(
                "OTP has expired."
            )

        if otp_obj.otp != otp:
            raise serializers.ValidationError(
                "Invalid OTP."
            )

        attrs["otp_obj"] = otp_obj

        return attrs

    def save(self):

        otp_obj = self.validated_data["otp_obj"]

        otp_obj.is_verified = True
        otp_obj.save()

        return otp_obj


class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ]

        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def validate_email(self, value):

        otp = EmailOTP.objects.filter(
            email=value,
            is_verified=True
        ).first()

        if not otp:
            raise serializers.ValidationError(
                "Email has not been verified."
            )

        return value

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        EmailOTP.objects.filter(
            email=validated_data["email"]
        ).delete()

        return user