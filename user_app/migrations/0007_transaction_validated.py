# Generated by Django 3.2 on 2022-10-20 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0006_auto_20221016_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='validated',
            field=models.BooleanField(default=False, verbose_name='validated'),
        ),
    ]
