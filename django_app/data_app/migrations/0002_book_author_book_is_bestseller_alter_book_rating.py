# Generated by Django 5.0.4 on 2024-05-11 12:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='is_bestseller',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
