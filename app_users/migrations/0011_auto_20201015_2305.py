# Generated by Django 2.2 on 2020-10-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0010_auto_20201015_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metatags',
            name='descriptor',
            field=models.CharField(max_length=21, null=True, verbose_name='тэги'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=150, verbose_name='название'),
        ),
    ]
