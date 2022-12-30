from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('like/<str:pk>', views.like_func, name='like'),
    path('dislike/<str:pk>', views.dislike_func, name='dislike'),
]