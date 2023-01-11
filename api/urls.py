from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.PostsView),

    path("locals/", views.LocalsView),
    path("local/products/<int:pk>/", views.LocalProductsView),
]
