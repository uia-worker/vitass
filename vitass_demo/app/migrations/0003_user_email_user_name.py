# Generated by Django 4.2.6 on 2023-10-22 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.EmailField(default="1", max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
