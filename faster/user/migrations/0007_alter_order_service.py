# Generated by Django 4.1 on 2023-02-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='service',
            field=models.CharField(choices=[('servic1', 'Service1'), ('service2', 'Service2'), ('service3', 'Service3')], max_length=20),
        ),
    ]
