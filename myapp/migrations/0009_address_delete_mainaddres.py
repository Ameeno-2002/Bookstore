# Generated by Django 5.1.1 on 2024-09-18 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_street_ad_mainaddres_street_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_ad', models.CharField(max_length=50)),
                ('state_ad', models.CharField(max_length=20)),
                ('coutry_name', models.CharField(max_length=37)),
            ],
        ),
        migrations.DeleteModel(
            name='MainAddres',
        ),
    ]
