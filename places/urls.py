from django.urls import path
from . import views

urlpatterns = [
    path('idex', views.index)
]