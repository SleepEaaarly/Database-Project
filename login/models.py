from django.db import models


# Create your models here.


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    # id:
    username = models.CharField(unique=True, max_length=128)
    # username: name of a user in this app
    real_name = models.CharField(max_length=128)
    # name: real name of a person
    password = models.CharField(max_length=256)
    # password
    sex_choice = (
        ('男', "男"),
        ('女', "女"),
    )
    sex = models.CharField(max_length=10, choices=sex_choice, default='男')
    # sex: male or female
    status = models.CharField(max_length=10)
    # status: init 0
    type = models.CharField(max_length=10)
    # type:


class PosPublisher(User):
    pass


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


class Teacher(PosPublisher):
    profession_title = models.CharField(max_length=128)
    # 职称
    research_direction = models.CharField(max_length=128)
    # 研究方向
    lab_belonging = models.ForeignKey("Lab", on_delete=models.CASCADE, blank=True, null=True)


class SchoolMate(PosPublisher):
    school_name = models.CharField(max_length=128)

    work_field = models.CharField(max_length=128)

    enterprise_belonging = models.ForeignKey("Enterprise", on_delete=models.CASCADE, blank=True, null=True)


class Enterprise(models.Model):
    id = models.CharField(primary_key=True, max_length=128)

    name = models.CharField(max_length=128)

    industry = models.CharField(max_length=128)


class Lab(models.Model):
    id = models.CharField(primary_key=True, max_length=128)

    name = models.CharField(max_length=128)


class Position(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    name = models.CharField(max_length=128)
    posPublisher = models.ForeignKey(PosPublisher, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=256)
    demanding = models.CharField(max_length=256)
    salary = models.CharField(max_length=32)
    place = models.CharField(max_length=128)
    label1 = models.CharField(max_length=128, blank=True, null=True)
    label2 = models.CharField(max_length=128, blank=True, null=True)
    label3 = models.CharField(max_length=128, blank=True, null=True)


class Post(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=1024)


class Resume(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    name = models.CharField(unique=True, max_length=128)
    edu_background = models.CharField(max_length=1024)
    per_statement = models.CharField(max_length=1024)
    experience = models.CharField(max_length=1024)
    sender = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=8)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)
    # init "0"


class Adminer(User):
    # todo
    pass


'''
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_sender", blank=True, null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_receiver", blank=True, null=True)
    content = models.CharField(max_length=256)
'''
