# Generated by Django 3.2 on 2022-09-14 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='student',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='requester', to='user_app.user'),
            preserve_default=False,
        ),
    ]