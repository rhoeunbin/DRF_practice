# Generated by Django 4.1.3 on 2022-11-30 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Board",
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
                ("title", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=30)),
                ("article", models.TextField(null=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
