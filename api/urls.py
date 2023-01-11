from django.urls import path
from . import views

urlpatterns = [
    path("post_view/", views.ProductView)
]