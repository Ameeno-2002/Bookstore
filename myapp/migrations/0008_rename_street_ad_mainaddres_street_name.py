# Generated by Django 5.1.1 on 2024-09-18 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_mainaddres_coutry_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainaddres',
            old_name='street_ad',
            new_name='street_name',
        ),
    ]
