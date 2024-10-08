# Generated by Django 5.1.1 on 2024-09-25 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='User name')),
                ('password', models.CharField(max_length=30, verbose_name='User password')),
                ('phone_number', models.CharField(max_length=11, unique=True)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=1, verbose_name="User's gender")),
                ('date_of_birth', models.DateField(verbose_name='Birth date')),
                ('profile_picture', models.ImageField(upload_to='', verbose_name='Profile image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='user.user')),
            ],
            options={
                'db_table': 'Profiles',
            },
        ),
    ]
