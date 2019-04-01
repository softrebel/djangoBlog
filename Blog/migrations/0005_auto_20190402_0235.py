# Generated by Django 2.1.7 on 2019-04-01 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20190402_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multimedia',
            name='multiMedia',
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='files/%Y-%m-%d/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/%Y-%m-%d/'),
        ),
    ]
