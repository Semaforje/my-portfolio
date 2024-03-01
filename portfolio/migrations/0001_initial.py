# Generated by Django 5.0.2 on 2024-03-01 14:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('short_desc', models.CharField(default='Placeholder', max_length=200)),
                ('description', ckeditor.fields.RichTextField(max_length=4000)),
                ('image', models.ImageField(upload_to='static/portfolio/images/')),
                ('project_link', models.CharField(blank=True, max_length=200, null=True)),
                ('github_link', models.CharField(blank=True, max_length=200, null=True)),
                ('project_details_image_1', models.ImageField(blank=True, null=True, upload_to='static/portfolio/images/')),
                ('project_details_image_2', models.ImageField(blank=True, null=True, upload_to='static/portfolio/images/')),
                ('project_details_check_image', models.ImageField(blank=True, null=True, upload_to='static/portfolio/images/')),
                ('project_details_github_image', models.ImageField(blank=True, null=True, upload_to='static/portfolio/images/')),
                ('tech_used', models.ManyToManyField(to='portfolio.technology')),
            ],
        ),
    ]
