# Generated by Django 4.1 on 2023-02-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('service', models.CharField(choices=[('service 1', 'Service 1'), ('service 2', 'Service 2'), ('service 3', 'Service 3')], max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Register1',
        ),
    ]
