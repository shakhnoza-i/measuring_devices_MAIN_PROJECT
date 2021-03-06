# Generated by Django 3.2.7 on 2021-10-14 10:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211014_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='address',
            field=models.TextField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='city',
            name='address',
            field=models.TextField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='device',
            name='description',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='dev_eui',
            field=models.CharField(default=0, max_length=16, validators=[django.core.validators.MinLengthValidator(16)]),
        ),
        migrations.AlterField(
            model_name='device',
            name='deviсe_type',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='district',
            name='address',
            field=models.TextField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='house',
            name='address',
            field=models.TextField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='house',
            name='name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='meter',
            name='serial_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meter',
            name='unit',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='street',
            name='address',
            field=models.TextField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='street',
            name='name',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
