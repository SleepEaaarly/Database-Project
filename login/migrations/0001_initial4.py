# Generated by Django 4.1.1 on 2022-12-10 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Enterprise",
            fields=[
                (
                    "id",
                    models.CharField(max_length=128, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=128)),
                ("industry", models.CharField(max_length=128)),
                ("place", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Lab",
            fields=[
                (
                    "id",
                    models.CharField(max_length=128, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Resume",
            fields=[
                (
                    "id",
                    models.CharField(max_length=128, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=128, unique=True)),
                ("content", models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.CharField(max_length=128, primary_key=True, serialize=False),
                ),
                ("username", models.CharField(max_length=128, unique=True)),
                ("real_name", models.CharField(max_length=128)),
                ("password", models.CharField(max_length=256)),
                (
                    "sex",
                    models.CharField(
                        choices=[("male", "男"), ("female", "女")],
                        default="male",
                        max_length=10,
                    ),
                ),
                ("type", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Adminer",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="login.user",
                    ),
                ),
            ],
            bases=("login.user",),
        ),
        migrations.CreateModel(
            name="PosPublisher",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="login.user",
                    ),
                ),
            ],
            bases=("login.user",),
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="login.user",
                    ),
                ),
                ("school_name", models.CharField(max_length=128)),
                (
                    "grade",
                    models.CharField(
                        choices=[
                            ("l_one", "大一"),
                            ("l_two", "大二"),
                            ("l_three", "大三"),
                            ("l_four", "大四"),
                            ("m_one", "研一"),
                            ("m_two", "研二"),
                            ("m_three", "研三"),
                            ("h_one", "博一"),
                            ("h_two", "博二"),
                        ],
                        default="大四",
                        max_length=10,
                    ),
                ),
                ("major", models.CharField(max_length=128)),
            ],
            bases=("login.user",),
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.CharField(max_length=128, primary_key=True, serialize=False),
                ),
                ("content", models.CharField(max_length=1024)),
                ("last_update_time", models.DateTimeField()),
                (
                    "last_update_user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="login.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Resume_Receiver",
            fields=[
                (
                    "id",
                    models.CharField(max_length=128, primary_key=True, serialize=False),
                ),
                (
                    "resume",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="login.resume"
                    ),
                ),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="login.pospublisher",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="resume",
            name="receiver",
            field=models.ManyToManyField(
                through="login.Resume_Receiver", to="login.pospublisher"
            ),
        ),
        migrations.AddField(
            model_name="resume",
            name="sender",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="login.student",
            ),
        ),
        migrations.CreateModel(
            name="Position",
            fields=[
                (
                    "id",
                    models.CharField(max_length=128, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=128)),
                ("description", models.CharField(max_length=256)),
                ("demanding", models.CharField(max_length=256)),
                ("salary", models.CharField(max_length=32)),
                (
                    "posPublisher",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="login.pospublisher",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "pospublisher_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="login.pospublisher",
                    ),
                ),
                ("profession_title", models.CharField(max_length=128)),
                ("research_direction", models.CharField(max_length=128)),
                (
                    "lab_belonging",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="login.lab",
                    ),
                ),
            ],
            bases=("login.pospublisher",),
        ),
        migrations.CreateModel(
            name="SchoolMate",
            fields=[
                (
                    "pospublisher_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="login.pospublisher",
                    ),
                ),
                ("school_name", models.CharField(max_length=128)),
                ("work_field", models.CharField(max_length=128)),
                (
                    "enterprise_belonging",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="login.enterprise",
                    ),
                ),
            ],
            bases=("login.pospublisher",),
        ),
    ]