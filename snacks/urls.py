from django.contrib import admin
from django.urls import path
from .views import HomePageView, SnackDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='snacks'),
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
]
