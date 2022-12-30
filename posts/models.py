#django
from django.db import models

#selfmade
from users.models import Account
# Create your models here.

def get_image_filepath(self, filename):
    return f'posts/static/posts/{self.owner.id}/{self.pk}.png'                                  #path user.id --> post.id
                                                                                                #issue with adding photo before uploading a post, post.id then is None
class Post(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    body = models.TextField()
    image = models.ImageField(max_length=255, upload_to=get_image_filepath, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.owner} | {self.title}'

    class Meta:
        ordering = ['-added']


class Coment(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    comented_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=256)
    addes = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.owner}, {self.comented_post}'


class Like(models.Model):
    person = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.person}, {self.post}'


class Dislike(models.Model):
    person = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    disliked = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.person}, {self.post}'