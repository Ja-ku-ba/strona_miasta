from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.PostsView),

    path("locals/", views.LocalsView),
    path("local/products/", views.LocalProductsView),
    path("local/products/<int:pk>/", views.ProductView),



    path('add/district/', views.add_district),
    path('add/street/', views.add_street),
    path('add/local/', views.add_local),
]
