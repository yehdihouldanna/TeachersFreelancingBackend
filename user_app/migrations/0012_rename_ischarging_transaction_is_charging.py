# Generated by Django 3.2 on 2022-09-09 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0011_alter_transaction_destination_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='isCharging',
            new_name='is_charging',
        ),
    ]