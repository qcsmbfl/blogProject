# Generated by Django 4.2.4 on 2023-09-18 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_userinfo_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(default='9cbfa35e512097e2c4bcc210ed8eee50', max_length=32, verbose_name='密码'),
        ),
    ]
