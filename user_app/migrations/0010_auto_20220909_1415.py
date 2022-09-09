# Generated by Django 3.2 on 2022-09-09 14:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import user_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0009_auto_20220909_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='sending_account',
            new_name='account',
        ),
        migrations.AddField(
            model_name='transaction',
            name='isCharging',
            field=models.BooleanField(default=False, verbose_name='is_charging_transaction'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='txn_id',
            field=models.CharField(blank=True, max_length=50, verbose_name='TXN ID'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='wallet',
            field=models.CharField(choices=[('Bankily', 'Bankily'), ('Masrvi', 'Masrvi'), ('Sedad', 'Sedad'), ('SiteSpecific', 'SiteSpecific')], default='SiteSpecific', max_length=30, verbose_name='Wallet'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='destination_account',
            field=models.OneToOneField(blank=True, default=user_app.models.Transaction.default_platform_account, on_delete=django.db.models.deletion.CASCADE, related_name='receiving_account', to='user_app.account'),
        ),
        migrations.DeleteModel(
            name='ChargingTransaction',
        ),
    ]