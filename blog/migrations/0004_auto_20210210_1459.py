# Generated by Django 3.1.6 on 2021-02-10 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210210_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ManyToManyField(to='blog.Post'),
        ),
    ]
