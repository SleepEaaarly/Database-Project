# Generated by Django 4.1.3 on 2022-12-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0001_initial8"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="grade",
            field=models.CharField(
                choices=[
                    ("大一", "大一"),
                    ("大二", "大二"),
                    ("大三", "大三"),
                    ("大四", "大四"),
                    ("研一", "研一"),
                    ("研二", "研二"),
                    ("研三", "研三"),
                    ("博一", "博一"),
                    ("博二", "博二"),
                ],
                default="大四",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="sex",
            field=models.CharField(
                choices=[("男", "男"), ("女", "女")], default="男", max_length=10
            ),
        ),
    ]
