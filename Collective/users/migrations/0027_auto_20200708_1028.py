# Generated by Django 3.0.4 on 2020-07-08 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_auto_20200708_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Hey, I am new to Ace Students'),
        ),
    ]
