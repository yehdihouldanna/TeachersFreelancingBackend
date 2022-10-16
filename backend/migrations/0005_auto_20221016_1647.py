# Generated by Django 3.2 on 2022-10-16 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0004_disponibility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='file',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='author_name'),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('classe', models.CharField(choices=[('99', 'any'), ('0', 'Mahdhara'), ('1AF', '1AF'), ('2AF', '2AF'), ('3AF', '3AF'), ('4AF', '4AF'), ('5AF', '5AF'), ('6AF', '6AF'), ('1AS', '1AS'), ('2AS', '2AS'), ('3AS', '3AS'), ('4AS', '4AS'), ('5AS', '5AS'), ('6AS', '6AS'), ('7AS', '7AS')], max_length=30, null=True, verbose_name='classe')),
                ('file', models.FileField(blank=True, default=None, max_length=254, null=True, upload_to='./book_files', verbose_name='book_file')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.subject')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploader', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Document',
            },
        ),
    ]