# Generated by Django 3.0.4 on 2020-06-26 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200609_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(default='general', max_length=20),
        ),
    ]
