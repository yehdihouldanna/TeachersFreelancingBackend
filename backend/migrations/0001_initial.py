# Generated by Django 3.2 on 2022-11-13 13:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('classe', models.CharField(choices=[('any', 'any'), ('Mahdhara', 'Mahdhara'), ('1AF', '1AF'), ('2AF', '2AF'), ('3AF', '3AF'), ('4AF', '4AF'), ('5AF', '5AF'), ('6AF', '6AF'), ('1AS', '1AS'), ('2AS', '2AS'), ('3AS', '3AS'), ('4AS', '4AS'), ('5AS', '5AS'), ('6AS', '6AS'), ('7AS', '7AS')], max_length=30, null=True, verbose_name='classe')),
                ('author', models.CharField(blank=True, max_length=50, null=True, verbose_name='author_name')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='price')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('name', models.CharField(choices=[('any', 'any'), ('Mahdhara', 'Mahdhara'), ('1AF', '1AF'), ('2AF', '2AF'), ('3AF', '3AF'), ('4AF', '4AF'), ('5AF', '5AF'), ('6AF', '6AF'), ('1AS', '1AS'), ('2AS', '2AS'), ('3AS', '3AS'), ('4AS', '4AS'), ('5AS', '5AS'), ('6AS', '6AS'), ('7AS', '7AS')], max_length=25, primary_key=True, serialize=False, verbose_name='classe')),
            ],
            options={
                'verbose_name': 'Classe',
                'verbose_name_plural': 'Classes',
            },
        ),
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
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('classe', models.CharField(choices=[('any', 'any'), ('Mahdhara', 'Mahdhara'), ('1AF', '1AF'), ('2AF', '2AF'), ('3AF', '3AF'), ('4AF', '4AF'), ('5AF', '5AF'), ('6AF', '6AF'), ('1AS', '1AS'), ('2AS', '2AS'), ('3AS', '3AS'), ('4AS', '4AS'), ('5AS', '5AS'), ('6AS', '6AS'), ('7AS', '7AS')], max_length=30, null=True, verbose_name='classe')),
                ('file', models.FileField(max_length=254, upload_to='./document_files', verbose_name='document_file')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Document',
            },
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, unique=True, verbose_name='title')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='description')),
                ('teacher_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='teacher name')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='time')),
            ],
            options={
                'verbose_name': 'Formation',
                'verbose_name_plural': 'Formations',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, verbose_name='title')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='description')),
                ('adresse', models.CharField(blank=True, max_length=100, null=True, verbose_name='adresse')),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('On going', 'On going'), ('Completed', 'Completed')], default='Pending', max_length=30, verbose_name='status')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('content', models.CharField(max_length=300, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('adresse', models.CharField(blank=True, max_length=100, null=True, verbose_name='adresse')),
                ('phone', models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='phone')),
            ],
            options={
                'verbose_name': 'School',
                'verbose_name_plural': 'Schools',
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('name', models.CharField(choices=[('Autre', 'Autre'), ('A', 'Literature'), ('C', 'Mathématiques'), ('D', 'Sciences_Naturelles'), ('O', 'Sciences_Religieuses'), ('T', 'Technique')], max_length=50, primary_key=True, serialize=False, verbose_name='specialty')),
            ],
            options={
                'verbose_name': 'Specialty',
                'verbose_name_plural': 'Specialties',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('name', models.CharField(choices=[('All', 'Tout'), ('Mathematics', 'Mathématiques'), ('Physics and Chemistry', 'Physique Chimie'), ('Natural Sciences', 'Sciences Naturelles'), ('Arabic', 'Arabe'), ('French', 'Français'), ('English', 'Anglais'), ('Mahdhara', 'Mahdhara'), ('Other', 'Autre')], max_length=25, primary_key=True, serialize=False, verbose_name='subject')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='BookOrder',
            fields=[
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.order')),
            ],
            options={
                'verbose_name': 'BookOrder',
                'verbose_name_plural': 'BookOrders',
            },
        ),
        migrations.CreateModel(
            name='LessonOrder',
            fields=[
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.order')),
                ('hours', models.IntegerField(blank=True, default=2, null=True)),
                ('unit_price', models.IntegerField(blank=True, default=200, null=True)),
                ('students_count', models.IntegerField(blank=True, default=1, null=True)),
            ],
            options={
                'verbose_name': 'LessonOrder',
                'verbose_name_plural': 'LessonOrders',
            },
        ),
    ]
