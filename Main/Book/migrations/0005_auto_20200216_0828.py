# Generated by Django 3.0.2 on 2020-02-16 07:28

import Book.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0004_auto_20200215_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, validators=[Book.validators.page_validator]),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.CharField(max_length=10, validators=[Book.validators.date_validator]),
        ),
    ]
