from django.contrib import admin

from .models import Client, Comment, ClientFile

admin.site.register(Client)
admin.site.register(Comment)
admin.site.register(ClientFile)
# Register your models here.
