# Generated by Django 3.0.4 on 2020-06-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200526_1419'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CollegeDataBase',
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='I really need to change my bio'),
        ),
    ]
