# Generated by Django 3.2 on 2024-02-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_rename_state_listing_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
    ]
