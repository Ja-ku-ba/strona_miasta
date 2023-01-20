from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import MessagesRoom, Message, RoomDeleteAsk
from users.models import Account
# Create your views here.

@login_required
def create_room(request, pk):
    user_1 = Account.objects.get(id=request.user.id)                                               #user who wnants to talk, and creates room
    user_2 = Account.objects.get(id=pk)                                                            #user to who user1 wants to tallk
    
    if MessagesRoom.objects.filter(owner1=user_1, owner2=user_2).exists():                         #redirects user to chat room, if that exists
        room = MessagesRoom.objects.get(owner1=user_1, owner2=user_2)    
        if room is True:
            return redirect('chat', room.id)                          
    elif MessagesRoom.objects.filter(owner1=user_2, owner2=user_1).exists():                        
        room = MessagesRoom.objects.get(owner1=user_2, owner2=user_1)
        if room is True:
            return redirect('chat', room.id)
    
    # print(room) ------------check if room exixts, if yes then redirect to room pages

    room = MessagesRoom.objects.create(
        owner1 = user_1,
        owner2 = user_2
    )
    return redirect('chat', room.id)

@login_required
def room(request, pk):
    room = MessagesRoom.objects.get(id=pk)
    messages_users = Message.objects.filter(room=room)
    context = {'room':room, 'messages_users':messages_users}
    return render(request, 'message/chat.html', context)

@login_required
def message_add(request, room_id, user_id):
    users = MessagesRoom.objects.get(id=room_id)                                                   #its required to redirect user agian to chat page, user1, and user2 are inside this instance. ... 
    user = Account.objects.get(id = user_id)                                                       #... User1 and user2 are needed to use create_room function that returns chat page
    room = MessagesRoom.objects.get(id=room_id)
    Message.objects.create(
        room = room,
        person = user,
        body = request.POST.get('body')
    )
    if users.owner1.id != request.user.id:
        return redirect('chat', room.id)
    return redirect('chat', room.id)

@login_required
def messages_list(request):
    user_first = MessagesRoom.objects.filter(owner1 = request.user)
    user_second = MessagesRoom.objects.filter(owner2 = request.user)
    user_messages_rooms = user_first | user_second
    context = {'user_messages_rooms':user_messages_rooms}
    return render(request, 'message/chat_list.html', context)


@login_required
def ask(request, room_id):
    room = MessagesRoom.objects.get(id=room_id)
    ask = RoomDeleteAsk.objects.filter(room=room)
    #define second user
    if request.user != room.owner1:
        second_user = room.owner1
    else:
        second_user = room.owner2

    #if one user deleted an account
    if second_user is None:
        room.delete()
        messages.info(request, 'Chat został pomyślnie usunięty')
        return redirect('chat_list')

    if ask.exists():
        #chek is second user confirms, or first spam the button
        delete_confirmation = RoomDeleteAsk.objects.get(room=room)
        if delete_confirmation.user1_ask == second_user:
            room.delete()
            messages.info(request, 'Chat został pomyślnie usunięty')
            return redirect('chat_list')

        if delete_confirmation.user2_conf == second_user:
            room.delete()
            messages.info(request, 'Chat został pomyślnie usunięty')
            return redirect('chat_list')
        return redirect('chat_list')

    #if ask is just created
    RoomDeleteAsk.objects.create(
        room = room,
        user1_ask = request.user
    )
    messages.info(request, f'{second_user} otrzyma wiadomość z zapytanie o potwierdzenie usunięcia chatu')
    return redirect('chat_list')


