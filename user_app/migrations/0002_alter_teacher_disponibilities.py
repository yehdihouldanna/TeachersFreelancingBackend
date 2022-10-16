# Generated by Django 3.2 on 2022-10-15 17:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='disponibilities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredi', 'Mercredi'), ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi'), ('Samdi', 'Samdi'), ('Dimanche', 'Dimanche')], max_length=25, verbose_name='day'), blank=True, default=list, null=True, size=None),
        ),
    ]
