# Generated by Django 3.2.9 on 2021-11-10 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('morfis_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonInfoMixin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('commoninfomixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='morfis_core.commoninfomixin')),
                ('status', models.CharField(choices=[('OPEN', 'Создана'), ('WIP', 'В процеесе работы'), ('CLOSE', 'Выполнена')], default='OPEN', max_length=10)),
                ('id_number', models.CharField(max_length=255, verbose_name='Учетный номер')),
            ],
            bases=('morfis_core.commoninfomixin',),
        ),
    ]
