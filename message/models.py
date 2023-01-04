from django.db import models
from users.models import Account
# Create your models here.

class MessagesRoom(models.Model):
    owner1 = models.ForeignKey(Account, related_name="owner1", on_delete=models.SET_NULL, blank=True, null=True)
    owner2 = models.ForeignKey(Account, related_name="owner2", on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.owner1}, {self.owner2}'

class RoomDeleteAsk(models.Model):
    user1_ask = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='ask', null=True, blank=True)
    room = models.ForeignKey(MessagesRoom, on_delete=models.SET_NULL, null=True, blank=True)
    user2_conf = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='confirmation', null=True, blank=True)

    def __str__(self):
        return f'{self.room}'


class Message(models.Model):
    room = models.ForeignKey(MessagesRoom, on_delete=models.CASCADE)
    person = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return f'{self.body}'

    class Meta:
        ordering = ['-added']
