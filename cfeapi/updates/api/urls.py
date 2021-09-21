from django.contrib import admin
from django.urls import path
from .views import UpdateModelDetailAPIView, UpdateModelListAPIView

urlpatterns = [
    path('',UpdateModelListAPIView.as_view()), #api/updates
    path('<id>/', UpdateModelDetailAPIView.as_view()),
]
