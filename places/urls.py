from django.urls import path
from . import views

urlpatterns = [
    path('places_forms', views.places_forms, name='places_forms')
]