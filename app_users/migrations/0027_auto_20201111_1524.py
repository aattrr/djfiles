# Generated by Django 2.2 on 2020-11-11 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0026_auto_20201111_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='user',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
