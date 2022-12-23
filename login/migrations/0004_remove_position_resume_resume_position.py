# Generated by Django 4.1.1 on 2022-12-22 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0003_alter_student_grade_alter_user_sex"),
    ]

    operations = [
        migrations.RemoveField(model_name="position", name="resume",),
        migrations.AddField(
            model_name="resume",
            name="position",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="login.position",
            ),
        ),
    ]
