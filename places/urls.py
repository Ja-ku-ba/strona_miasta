from django.urls import path
from . import views

urlpatterns = [
    path('places_forms', views.places_forms, name='places_forms'),

    
    path('district_list', views.district_list, name='district_list'),
    path('district_form/<str:pk>', views.district, name='district_form'),
    
    path('street_list', views.street_list, name='street_list'),
    path('street_form/<str:pk>', views.street, name='street_form'),

    path('local_list', views.local_list, name='local_list'),
    path('local_form/<str:pk>', views.local_form, name='local_form'),
    path('local_add', views.local_add, name='local_add'),
    path('local_delete/<str:pk>', views.local_delete, name='local_delete'),
    
    path('product_list', views.product_list, name='product_list'),
    path('product_add', views.product_add, name='product_add'),
    path('product_edit/<str:pk>', views.product_edit, name='product_edit'),
    path('product_delete/<str:pk>', views.product_delete, name='product_delete'),
    
    path('rating_list', views.rating_list, name='rating_list'),
    path('rating_add', views.rating_add, name='rating_add'),
    path('rating_edit/<str:pk>', views.rating_edit, name='rating_edit'),
    path('rating_delete/<str:pk>', views.rating_delete, name='rating_delete'),
]