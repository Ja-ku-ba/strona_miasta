from django.contrib import admin
from .models import District, Street, Locals, LocalProducts, LocalStaff
# Register your models here.
admin.site.register(District)
admin.site.register(Street)
admin.site.register(Locals)
admin.site.register(LocalProducts)
admin.site.register(LocalStaff)