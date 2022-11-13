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

    grade = models.CharField(max_length=10, choices=grade_choice, default='大四')

    major = models.CharField(max_length=128)


class Teacher(User):
    profession_title = models.CharField(max_length=128)
    # 职称
    research_direction = models.CharField(max_length=128)
    # 研究方向
    lab_name = models.CharField(max_length=128)


class SchoolMate(User):
    school_name = models.CharField(max_length=128)

    work_field = models.CharField(max_length=128)


class Enterprise(models.Model):
    name = models.CharField(max_length=128)

    industry = models.CharField(max_length=128)
    # 所属行业
    place = models.CharField(max_length=128)
    

class Lab(models.Model):
    name = models.CharField(max_length=128)


class Post(models.Model):
    content = models.CharField(max_length=1024)
    last_update_time = models.DateTimeField()
    last_update_user = models.ForeignKey(User, on_delete=models.CASCADE)


class Resume(models.Model):
    content = models.CharField(max_length=1024)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Position(models.Model):
    name = models.CharField(max_length=128)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    demanding = models.CharField(max_length=256)
    salary = models.IntegerField()


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)


class Adminer(User):
    # todo
    pass