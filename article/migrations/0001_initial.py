# Generated by Django 5.1.1 on 2024-10-03 13:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='articles', to='article.category', verbose_name='Category')),
            ],
            options={
                'db_table': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='DailyCategorySummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='summary_text', to='article.category', verbose_name='Category')),
            ],
            options={
                'db_table': 'DailyCategorySummaries',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('status', models.BooleanField(verbose_name='Status')),
                ('summary', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='article.dailycategorysummary', verbose_name='Summary')),
            ],
            options={
                'db_table': 'Reports',
            },
        ),
        migrations.CreateModel(
            name='ReportLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('status', models.BooleanField(verbose_name='Status')),
                ('report', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='article.report', verbose_name='Report')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'ReportLines',
            },
        ),
    ]
