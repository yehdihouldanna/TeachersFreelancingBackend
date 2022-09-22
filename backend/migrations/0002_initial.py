# Generated by Django 3.2 on 2022-09-12 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0001_initial'),
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to='user_app.student'),
        ),
        migrations.AddField(
            model_name='formation',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.school'),
        ),
        migrations.AddField(
            model_name='document',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.subject'),
        ),
        migrations.AddField(
            model_name='lessonorder',
            name='subject',
            field=models.ManyToManyField(to='backend.Subject'),
        ),
    ]