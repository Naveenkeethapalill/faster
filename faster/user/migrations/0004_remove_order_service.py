# Generated by Django 4.1 on 2023-02-06 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='service',
        ),
    ]