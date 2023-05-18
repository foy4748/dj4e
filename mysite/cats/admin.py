from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Breed)
admin.site.register(models.Cat)
