from django.contrib import admin

from .models import Post, Coment, Like, Dislike, Interractions
# Register your models here.
admin.site.register(Post)
admin.site.register(Coment)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Interractions)

