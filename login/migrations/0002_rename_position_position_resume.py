# Generated by Django 4.1.1 on 2022-12-21 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0001_initial7"),
    ]

    operations = [
        migrations.RenameField(
            model_name="position", old_name="position", new_name="resume",
        ),
    ]
