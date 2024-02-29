# Generated by Django 5.0.1 on 2024-02-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tech_used',
            field=models.ManyToManyField(to='portfolio.tech'),
        ),
    ]
