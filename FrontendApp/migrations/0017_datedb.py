# Generated by Django 5.1 on 2024-09-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontendApp', '0016_item_addeddb_datepicker'),
    ]

    operations = [
        migrations.CreateModel(
            name='dateDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datepicker', models.DateField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
