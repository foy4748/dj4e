from django.contrib import admin

# Register your models here.

from .models import Ad, Comment

admin.site.register(Ad)
admin.site.register(Comment)
