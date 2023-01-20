from django.urls import path
from . import views

urlpatterns = [
    path('stwórz/rozmowa/<str:pk>', views.create_room, name='create_room'),
    path('rozmowy', views.messages_list, name='chat_list'),
    path('rozmowa/<int:pk>', views.room, name='chat'),
    
    path('wyslij_wiadomosc/<str:room_id>/<str:user_id>', views.message_add, name='message_add'),

    path('usun_chat/<str:room_id>', views.ask, name='delete_chat')
]