from django.urls import path
from .views import register_view
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', register_view),
    path('login/', TokenObtainPairView.as_view()),
]

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)