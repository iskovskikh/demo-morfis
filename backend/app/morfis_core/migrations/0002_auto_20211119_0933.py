# Generated by Django 3.2.9 on 2021-11-19 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('morfis_core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='request_timestamp',
            new_name='timestamp',
        ),
        migrations.AlterField(
            model_name='icdcode',
            name='disease_description',
            field=models.CharField(max_length=255, verbose_name='Описание диагнозa'),
        ),
        migrations.CreateModel(
            name='PreviousCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=255, verbose_name='Организация, давшая заключение')),
                ('timestamp', models.DateTimeField(verbose_name='Дата заключения')),
                ('request_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Регистрационный номер заключения')),
                ('conclusion', models.TextField(verbose_name='Заключение')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='morfis_core.case', verbose_name='Организация, давшая заключение')),
            ],
        ),
    ]