# Generated by Django 3.2.7 on 2021-10-04 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211003_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='uuid_deviсe',
            new_name='uuid',
        ),
        migrations.RenameField(
            model_name='meter',
            old_name='uuid_meter',
            new_name='uuid',
        ),
    ]