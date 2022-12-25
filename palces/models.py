from django.db import models
from users.models import Account
# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=64)


class Street(models.Model):
    name = models.CharField(max_length=128)
    street_district = models.ForeignKey(District, on_delete=models.SET_NULL)


class Locals(models.Model):
    name = models.CharField(max_length=128)
    local_street = models.ForeignKey(Street, on_delete=models.SET_NULL)
    local_addres = models.CharField(max_length=16)
    local_ovners = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    local_workers = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)


class LocalProducts(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.CharField(max_length=16)
    product_local = models.ForeignKey(Locals, on_delete=models.CASCADE)