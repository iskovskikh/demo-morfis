# Generated by Django 3.2.9 on 2021-12-09 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='CommonInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commoninfo_requests_created', to=settings.AUTH_USER_MODEL)),
                ('lastmodified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commoninfo_requests_modified', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название учереждения')),
                ('address', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='morfis_core.address', verbose_name='Адресс учереждения')),
            ],
            options={
                'verbose_name': 'Учереждение',
                'verbose_name_plural': 'Учереждения',
            },
        ),
        migrations.CreateModel(
            name='IcdCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, verbose_name='Код диагноза')),
                ('disease_description', models.CharField(max_length=255, verbose_name='Описание диагнозa')),
                ('parent_code', models.CharField(max_length=255, verbose_name='Код родителя')),
            ],
            options={
                'verbose_name': 'Код международной классификации болезней',
                'verbose_name_plural': 'Коды международной классификации болезней',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='morfis_core.commoninfo')),
                ('status', models.CharField(choices=[('OPEN', 'Создана'), ('SENDED', 'Направлена'), ('ACCEPTED', 'Принята'), ('ARCHIVED', 'Архивирована'), ('CLOSE', 'Выполнена')], default='OPEN', max_length=10)),
                ('request_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Регистрационный номер случая')),
                ('timestamp', models.DateTimeField(verbose_name='Дата направления')),
                ('disease_description', models.TextField(verbose_name='Диагноз заболевания (состояния)')),
                ('order_task', models.TextField(verbose_name='Задача исследования')),
                ('hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='morfis_core.hospital', verbose_name='Филиал')),
                ('mkb_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='morfis_core.icdcode', verbose_name='Код МКБ')),
            ],
            options={
                'verbose_name': 'Случай',
                'verbose_name_plural': 'Случаи',
            },
            bases=('morfis_core.commoninfo',),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название организации')),
                ('address', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='morfis_core.address', verbose_name='Адрес организации')),
                ('hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='morfis_core.hospital', verbose_name='Лаборатория')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
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
        migrations.AddField(
            model_name='case',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='morfis_core.organization', verbose_name='Организация'),
        ),
    ]
