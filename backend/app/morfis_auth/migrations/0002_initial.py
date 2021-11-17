# Generated by Django 3.2.9 on 2021-11-17 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('morfis_auth', '0001_initial'),
        ('morfis_core', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='morfisuser',
            name='subdivision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='morfis_core.subdivision', verbose_name='Филиал'),
        ),
        migrations.AddField(
            model_name='morfisuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
