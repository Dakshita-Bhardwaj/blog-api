from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView

from .views import (
    SendOTPView,
    VerifyOTPView,
    RegisterView,
)

urlpatterns = [
    path("send-otp/", SendOTPView.as_view()),
    path("verify-otp/", VerifyOTPView.as_view()),
    path("register/", RegisterView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
]