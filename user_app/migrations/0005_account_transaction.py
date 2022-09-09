# Generated by Django 3.2 on 2022-08-18 17:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_auto_20220816_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user_app.user')),
                ('account_number', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('balance', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_account_number', models.UUIDField()),
                ('amount_MRU', models.IntegerField()),
                ('sending_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='user_app.account')),
            ],
        ),
    ]
