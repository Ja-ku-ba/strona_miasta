from django.urls import path
from . import views

urlpatterns = [
    path('coment_add', views.coment_add, name='coment_add'),

    path('post_add', views.post_add, name='post_add'),
    # path('post_edit/<str:pk>', views.post_edit, name='post_edit'),
    path('post_delete/<str:pk>/<str:user_req>', views.post_delete, name='post_delete'),
    
    path('coment_add/<str:pk>', views.coment_add, name='coment_add'),
    path('coment_delete/<str:pk>/<str:user_req>', views.coment_delete, name='coment_delete'),
]