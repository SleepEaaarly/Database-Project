# Register your models here.

from . import models
from django.contrib import admin

admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Lab)
admin.site.register(models.Enterprise)
admin.site.register(models.SchoolMate)
admin.site.register(models.Post)
admin.site.register(models.Resume)
admin.site.register(models.Position)
admin.site.register(models.Message)
