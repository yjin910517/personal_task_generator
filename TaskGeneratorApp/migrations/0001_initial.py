# Generated by Django 4.2.7 on 2023-11-30 03:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('io_type', models.CharField(max_length=255)),
                ('task_name', models.TextField()),
                ('deliverable', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('duration', models.IntegerField(validators=[django.core.validators.MaxValueValidator(120), django.core.validators.MinValueValidator(1)])),
                ('effort_level', models.SmallIntegerField()),
                ('last_chosen_date', models.DateField()),
            ],
        ),
    ]
