from django.shortcuts import render, redirect

from .models import MessagesRoom, Message
from users.models import Account
# Create your views here.

def create_room(request, pk):
    user_1 = Account.objects.get(id=request.user.id)                                               #user who wnants to talk, and creates room
    user_2 = Account.objects.get(id=pk)                                                            #user to who user1 wants to tallk
    
    if MessagesRoom.objects.filter(owner1=user_1, owner2=user_2).exists():
        room = MessagesRoom.objects.get(owner1=user_1, owner2=user_2)                              #redirects user to chat room, if that exists
    elif MessagesRoom.objects.filter(owner1=user_2, owner2=user_1).exists():
        room = MessagesRoom.objects.get(owner1=user_2, owner2=user_1)
    else:
        room = MessagesRoom.objects.create(
            owner1 = user_1,
            owner2 = user_2
        )
    messages_users = room.message_set.all()
    context = {'messages_users':messages_users, 'room':room, 'user_1':user_1}
    return render(request, 'core/chat.html', context)


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
        return redirect('create_room', users.owner1.id)
    return redirect('create_room', users.owner2.id)


def messages_list(request):
    user_first = MessagesRoom.objects.filter(owner1 = request.user)
    user_second = MessagesRoom.objects.filter(owner2 = request.user)
    user_messages_rooms = user_first | user_second
    context = {'user_messages_rooms':user_messages_rooms}
    return render(request, 'message/chat_list.html', context)

def delete_chat(request, second_user_id):
    user_second = Account.objects.get(id=second_user_id)
    try:
        room = MessagesRoom.objects.get(owner1=request.user, owner2=user_second)
        
    except:
        room = MessagesRoom.objects.get(owner1=user_second, owner1=request.user)

    return render('')