from django.db import models
from users.models import Account
# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=128)
    street_district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

def get_logo_image_filepath(self, filename):
    return f'static/locals/{self.pk}/logo.png'                           #route places/static/locals/local.id/logo.png

class Locals(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    local_street = models.ForeignKey(Street, on_delete=models.SET_NULL, null=True, blank=True)
    local_addres = models.CharField(max_length=16)
    logo = models.ImageField(max_length=255, upload_to=get_logo_image_filepath, null=True, blank=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def street(self):
        return self.local_street.name

def get_profile_product_image_filepath(self, filename):
    return f'static/locals/{self.product_local.id}/products/{self.pk}.png'                           #route places/static/locals/local.id/products/product.id.png

class LocalProducts(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=16, null=True, blank=True)
    product_local = models.ForeignKey(Locals, on_delete=models.CASCADE)
    product_image = models.ImageField(max_length=255, upload_to=get_profile_product_image_filepath, null=True, blank=True)

    def __str__(self):
        return self.name


class LocalRating(models.Model):
    opinion = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    local = models.ForeignKey(Locals, on_delete=models.CASCADE)
    person = models.ForeignKey(Account, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.local}, {self.person}'

    class Meta:
        ordering = ['-added']

class LocalProductRating(models.Model):
    opinion = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey(LocalProducts, on_delete=models.CASCADE)
    person = models.ForeignKey(Account, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product}, {self.person}'

    class Meta:
        ordering = ['-added']


class PlaceToVisit(models.Model):
    local = models.ForeignKey(Locals, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    want_to_visit = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)

class PlaceFavourite(models.Model):
    local = models.ForeignKey(Locals, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    user_like = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)