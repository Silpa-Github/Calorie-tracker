# Generated by Django 5.1 on 2024-08-25 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontendApp', '0006_alter_caloriedb_age_alter_caloriedb_calorie_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='number_basis_foodDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
