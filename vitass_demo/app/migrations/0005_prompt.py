# Generated by Django 4.2.6 on 2023-10-26 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_user_telehpone"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prompt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=200)),
                ("title", models.CharField(max_length=200)),
                ("text", models.CharField(max_length=500)),
            ],
        ),
    ]
