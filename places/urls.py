from django.urls import path
from . import views

urlpatterns = [
    path('places_forms', views.places_forms, name='places_forms'),

    
    path('district_list', views.district_list, name='district_list'),
    path('district_form/<str:pk>', views.district, name='district_form'),
]