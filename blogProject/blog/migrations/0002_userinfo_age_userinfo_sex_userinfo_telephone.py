# Generated by Django 4.2.4 on 2023-08-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=0, verbose_name='年龄'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='sex',
            field=models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '保密')], default=3, verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='telephone',
            field=models.CharField(default='', max_length=11, verbose_name='电话号码'),
        ),
    ]
