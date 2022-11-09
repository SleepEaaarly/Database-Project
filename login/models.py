from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    # id: primary key
    real_name = models.CharField(max_length=128)
    # name: real name of a person
    username = models.CharField(max_length=128)
    # username: name of a user in this app
    password = models.CharField(max_length=256)
    # password
    email = models.EmailField(unique=True)
    # email
    sex_choice = (
        ('male', "男"),
        ('female', "女"),
    )
    sex = models.CharField(max_length=10, choices=sex_choice, default='male')
    # sex: male or female


    class Meta:
        ordering = ["id"]
        verbose_name = "用户"
        verbose_name_plural = verbose_name