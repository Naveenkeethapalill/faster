# Generated by Django 4.1 on 2023-02-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_test_name_test_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='service',
            field=models.CharField(choices=[('service 1', 'Service 1'), ('service 2', 'Service 2'), ('service 3', 'Service 3')], max_length=20),
        ),
    ]
