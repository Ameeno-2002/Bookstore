# Generated by Django 5.1.1 on 2024-09-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_address_delete_mainaddres'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_img', models.ImageField(upload_to='')),
                ('prod_name', models.TextField(max_length=45)),
                ('prod_time', models.TimeField()),
            ],
        ),
    ]
