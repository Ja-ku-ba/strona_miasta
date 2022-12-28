from django.urls import path
from . import views

urlpatterns = [
    path('post_coment', views.post_coment, name='post_coment'),
    path('coment_add', views.coment_add, name='coment_add'),

    path('posts_list', views.posts_list, name='posts_list'),
    path('post_add', views.post_add, name='post_add'),
    path('post_edit/<str:pk>', views.post_edit, name='post_edit'),
    path('post_delete/<str:pk>', views.post_delete, name='post_delete'),
    
    path('coment_list', views.coment_list, name='coment_list'),
    path('coment_add/<str:pk>', views.coment_add, name='coment_add'),
    path('coment_delete/<str:pk>', views.coment_delete, name='coment_delete'),
]