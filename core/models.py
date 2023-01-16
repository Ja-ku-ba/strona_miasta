from django.db import models

from users.models import Account
from posts.models import Post
from message.models import MessagesRoom, RoomDeleteAsk

from places.models import LocalRating, LocalProductRating
# Create your models here.


class UserNotifications(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post)
    messages = models.ManyToManyField(MessagesRoom)
    messages_room_ask = models.ManyToManyField(RoomDeleteAsk)

    def __str__(self) -> str:
        return f"{self.user.username}"


