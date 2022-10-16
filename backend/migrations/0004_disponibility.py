# Generated by Django 3.2 on 2022-10-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_specialty_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disponibility',
            fields=[
                ('name', models.CharField(choices=[('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredi', 'Mercredi'), ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi'), ('Samdi', 'Samdi'), ('Dimanche', 'Dimanche')], max_length=25, primary_key=True, serialize=False, verbose_name='day')),
            ],
            options={
                'verbose_name': 'Disponibility',
                'verbose_name_plural': 'Disponibilities',
            },
        ),
    ]
