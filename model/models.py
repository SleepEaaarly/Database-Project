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
        abstract = True
        ordering = ["id"]
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class Student(User):
    school_name = models.CharField(max_length=128)

    grade_choice = (
        ('大一', '大一'),
        ('大二', '大二'),
        ('大三', '大三'),
        ('大四', '大四'),
        ('研一', '研一'),
        ('研二', '研二'),
        ('研三', '研三'),
        ('博一', '博一'),
        ('博二', '博二'),
    )

    grade = models.CharField(max_length=10, choices=grade_choice, default='大一')

    major = models.CharField(max_length=128)


class Teacher(User):


class SchoolMate(User):


class Adminer(User):