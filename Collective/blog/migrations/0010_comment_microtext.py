# Generated by Django 3.0.4 on 2020-07-07 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200708_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='microtext',
            field=models.CharField(blank=True, default='Entry by me', max_length=20),
        ),
    ]
