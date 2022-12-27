from django.urls import path
from . import views

urlpatterns = [
    path('posts_list', views.posts_list, name='posts_list'),
    path('post_add', views.post_add, name='post_add'),
    path('post_edit/<str:pk>', views.post_edit, name='post_edit'),
    path('post_delete/<str:pk>', views.post_delete, name='post_delete'),
]