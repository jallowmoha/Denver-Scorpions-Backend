# Generated by Django 3.2.3 on 2021-05-30 18:12

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('home_team', models.CharField(default='', max_length=35)),
                ('away_team', models.CharField(default='', max_length=35)),
                ('logo', models.ImageField(default='', storage=django.core.files.storage.FileSystemStorage, upload_to='')),
                ('game_time', models.DateTimeField()),
                ('game_location', models.CharField(blank=True, default='', max_length=20)),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
    ]
