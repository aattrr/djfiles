# Generated by Django 2.2 on 2020-10-29 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0019_auto_20201028_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='count_news',
        ),
    ]
