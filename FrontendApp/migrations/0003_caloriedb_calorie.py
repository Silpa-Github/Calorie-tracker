# Generated by Django 5.1 on 2024-08-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontendApp', '0002_caloriedb'),
    ]

    operations = [
        migrations.AddField(
            model_name='caloriedb',
            name='calorie',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
