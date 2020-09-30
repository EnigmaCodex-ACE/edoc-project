# Generated by Django 3.0.4 on 2020-06-09 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20200609_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='commentimg',
            field=models.ImageField(default='', upload_to='comment_img', verbose_name='Comment Image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]