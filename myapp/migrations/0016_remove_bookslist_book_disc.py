# Generated by Django 5.1.1 on 2024-09-19 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_bookslist_book_disc_alter_bookslist_book_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookslist',
            name='book_disc',
        ),
    ]
