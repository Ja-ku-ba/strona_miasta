from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:pk>', views.post, name='post'),
    path('like/<str:pk>', views.like_func, name='like'),
    path('dislike/<str:pk>', views.dislike_func, name='dislike'),
    
    path('search/', views.search, name='search'),

    path('uzytkownik/<str:name>', views.user_page, name='user_page')
]