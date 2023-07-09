from django.contrib import admin
from django.urls import path
from .views import ProductAPIView, UserAPIView

urlpatterns = [
    path('products', ProductAPIView.as_view()),
    path('products/<str:pk>', ProductAPIView.as_view()),
    path('user', UserAPIView.as_view())
]
