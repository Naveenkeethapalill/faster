# Generated by Django 4.1 on 2023-02-06 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]