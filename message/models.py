from django.db import models

from users.models import Account
# Create your models here.

class MessagesRoom(models.Model):
    owners = models.ManyToManyField(Account)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owners}'


class Message(models.Model):
    room = models.ForeignKey(MessagesRoom, on_delete=models.CASCADE)
    person = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return f'{self.body}'

    class Meta:
        ordering = ['-added']
