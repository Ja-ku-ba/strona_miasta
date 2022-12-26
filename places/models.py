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


class Locals(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    local_street = models.ForeignKey(Street, on_delete=models.SET_NULL, null=True, blank=True)
    local_addres = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class LocalStaff(models.Model):
    person = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    local = models.ForeignKey(Locals, on_delete=models.CASCADE)
    local_ovners = models.BooleanField(null=True, blank=True)
    local_workers = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.person, self.local


class LocalProducts(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=16, null=True, blank=True)
    product_local = models.ForeignKey(Locals, on_delete=models.CASCADE)

    def __str__(self):
        return self.name