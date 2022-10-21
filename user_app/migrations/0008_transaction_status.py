# Generated by Django 3.2 on 2022-10-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_transaction_validated'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Validated', 'Validated')], default='Pending', max_length=30, verbose_name='Status'),
        ),
    ]
