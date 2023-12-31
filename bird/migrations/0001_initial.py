# Generated by Django 4.2.4 on 2023-08-03 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bird",
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
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Название птицы"),
                ),
                ("color", models.CharField(max_length=50, verbose_name="Цвет перьев")),
                (
                    "photo",
                    models.ImageField(
                        upload_to="bird_photos/", verbose_name="Фотография"
                    ),
                ),
                (
                    "sightings",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Количество наблюдений"
                    ),
                ),
            ],
            options={
                "verbose_name": "Птица",
                "verbose_name_plural": "Птицы",
            },
        ),
    ]
