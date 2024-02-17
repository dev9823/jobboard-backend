# Generated by Django 5.0.2 on 2024-02-16 18:23

import autoslug.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_user_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='user', unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='jobseekers/images')),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('resume', models.FileField(upload_to='resume/')),
            ],
        ),
    ]