# Generated by Django 4.1.7 on 2023-03-23 22:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ShortenedUrl",
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
                ("original_url", models.URLField()),
                ("shortened_url", models.URLField()),
                ("token", models.CharField(max_length=6, unique=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("clicks", models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
