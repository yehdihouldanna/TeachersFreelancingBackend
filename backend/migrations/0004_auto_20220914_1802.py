# Generated by Django 3.2 on 2022-09-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20220914_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='subject',
        ),
        migrations.AddField(
            model_name='subject',
            name='name',
            field=models.CharField(choices=[('All', 'Tout'), ('Maths', 'Mathématiques'), ('Physics_and_Chemistry', 'Physique Chimie'), ('Natural_Sciences', 'Sciences Naturelles'), ('Arabic', 'Arabe'), ('French', 'Français'), ('English', 'Anglais'), ('Mahdhara', 'Mahdhara'), ('Other', 'Autre')], default=0, max_length=25, primary_key=True, serialize=False, verbose_name='subject'),
            preserve_default=False,
        ),
    ]