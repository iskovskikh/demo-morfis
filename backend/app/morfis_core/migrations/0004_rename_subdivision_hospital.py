# Generated by Django 3.2.9 on 2021-11-25 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('morfis_auth', '0003_position'),
        ('morfis_core', '0003_auto_20211125_1142'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subdivision',
            new_name='Hospital',
        ),
    ]