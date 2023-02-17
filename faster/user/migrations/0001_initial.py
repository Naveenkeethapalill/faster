# Generated by Django 4.1 on 2023-01-31 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('plocation', models.CharField(max_length=50)),
                ('dlocation', models.CharField(max_length=50)),
                ('plan', models.IntegerField(max_length=4)),
            ],
        ),
    ]