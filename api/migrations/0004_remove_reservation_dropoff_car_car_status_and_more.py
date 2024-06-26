# Generated by Django 4.1.3 on 2024-03-24 06:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_reservation_payment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reservation",
            name="dropoff",
        ),
        migrations.AddField(
            model_name="car",
            name="car_status",
            field=models.CharField(
                choices=[("BOOKED", "Booked"), ("FREE", "Free")],
                default="FREE",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="hours",
            field=models.IntegerField(default=1),
        ),
    ]
