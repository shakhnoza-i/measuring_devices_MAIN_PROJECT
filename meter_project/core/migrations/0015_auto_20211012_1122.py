# Generated by Django 3.2.7 on 2021-10-12 11:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20211012_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='full_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='city',
            name='full_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='district',
            name='full_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='house',
            name='full_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='street',
            name='full_owner',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, size=None),
        ),
    ]
