# Generated by Django 3.2 on 2022-09-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20220922_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='title',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='title'),
        ),
    ]