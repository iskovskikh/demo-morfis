# Generated by Django 3.2.9 on 2022-02-01 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('morfis_core', '0003_organization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='hospital',
        ),
    ]
