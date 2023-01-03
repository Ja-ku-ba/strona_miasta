from django.db import models

from users.models import Account
# Create your models here.

class MessagesRoom(models.Model):
    owner1 = models.ForeignKey(Account, related_name="owner1", on_delete=models.SET_NULL, blank=True, null=True)
    deleted1 = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    owner2 = models.ForeignKey(Account, related_name="owner2", on_delete=models.SET_NULL, blank=True, null=True)
    deleted2 = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)



class Message(models.Model):
    room = models.ForeignKey(MessagesRoom, on_delete=models.CASCADE)
    person = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return f'{self.body}'

    class Meta:
        ordering = ['-added']
