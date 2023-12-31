# Generated by Django 4.2.4 on 2023-08-18 15:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Workers",
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
                ("name", models.CharField(max_length=50)),
                ("position", models.CharField(max_length=50)),
                ("working_hours_month", models.FloatField()),
                ("holiday_this_month", models.BooleanField(default=False)),
            ],
        ),
    ]
