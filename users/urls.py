from django.urls import path
from . import views

urlpatterns = [
    path('zarejestruj', views.register, name='register'),
    path('zaloguj', views.login_user, name='login'),
    path('wyloguj', views.logout_user, name='logout'),
]