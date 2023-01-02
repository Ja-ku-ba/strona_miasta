from django.contrib import admin

from message.models import MessagesRoom, Message
# Register your models here.
admin.site.register(MessagesRoom)
admin.site.register(Message)