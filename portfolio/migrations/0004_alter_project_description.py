# Generated by Django 5.0.1 on 2024-02-08 18:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_rename_tech_technology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=4000),
        ),
    ]