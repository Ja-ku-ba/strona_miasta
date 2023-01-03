from django.urls import path
from . import views

urlpatterns = [
    path('chat/<str:pk>', views.create_room, name='create_room'),
    path('rozmowa', views.messages_list, name='chat_list'),
    
    path('wyslij_wiadomosc/<str:room_id>/<str:user_id>', views.message_add, name='message_add'),

]