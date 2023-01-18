#django
from django.db import models

#selfmade
from users.models import Account
# Create your models here.

def get_image_filepath(self, filename):
    return f'posts/static/posts/{self.owner.id}/{self.pk}.png'                                  #path user.id --> post.id
                                                                                                #isue with adding photo before uploading a post, post.id then is None
class Post(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    body = models.TextField()
    image = models.ImageField(max_length=255, upload_to=get_image_filepath, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    reactions = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.owner} | {self.title}'

    class Meta:
        ordering = ['-added']

        
    @property
    def owner_post(self):
        return Account.objects.get(id=self.owner.id).username


class Coment(models.Model):
    post_owner = models.ForeignKey(Account, related_name="post_owner_coment", on_delete=models.CASCADE)                         #required due to notifications, this one line erases entire notifications app and models
    owner = models.ForeignKey(Account, related_name="owner_coment", on_delete=models.CASCADE)
    comented_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=256)
    added = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.owner}, {self.comented_post}'

    class Meta:
        ordering = ['-added']

class Like(models.Model):
    post_owner = models.ForeignKey(Account, related_name="post_owner_like", on_delete=models.CASCADE)               #required due to notifications, this one line erases entire notifications app and models
    person = models.ForeignKey(Account, related_name="person_like", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.person}, {self.post}'

    class Meta:
        ordering = ['-added']


class Dislike(models.Model):
    post_owner = models.ForeignKey(Account, related_name="post_owner_dislike", on_delete=models.CASCADE)                    #required due to notifications, this one line erases entire notifications app and models
    person = models.ForeignKey(Account, related_name="person_dislike", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.person}, {self.post}'

    class Meta:
        ordering = ['-added']


class Interractions(models.Model):
    person = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.person}, {self.post}'

    class Meta:
        ordering = ['-added']