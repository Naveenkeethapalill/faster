# Generated by Django 4.1 on 2023-02-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_test_name_test_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='name',
            field=models.CharField(default='exit', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='service',
            field=models.CharField(choices=[('servic1', 'Service1'), ('service2', 'Service2'), ('service3', 'Service3')], default='exit', max_length=20),
            preserve_default=False,
        ),
    ]
