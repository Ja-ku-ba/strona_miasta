#django
from django.db import models

#selfmade
from users.models import Account
# Create your models here.

class Post(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    body = models.TextField()
    # image = 
    added = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.owner} | {self.title}'


class Coment(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    comented_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=256)
    addes = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.owner}, {self.comented_post}'