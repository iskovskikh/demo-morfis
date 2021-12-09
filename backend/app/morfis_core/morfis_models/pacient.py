from django.db import models

from morfis_core.morfis_models.hospital import Hospital


class Pacient(models.Model):

    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Имя'
    )
    middle_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Отчество'
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Фамилия'
    )

    mis_id = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        verbose_name='МИС индификатор'
    )
    mis_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='МИС номер'
    )
    oms_number = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='ОМС номер'
    )
    snils_number = models.CharField(
        max_length=255,
        blank=True,
        default='',
        verbose_name='СНИЛС номер'
    )
    phone = models.CharField(
        max_length=255,
        blank=True,
        default='',
        verbose_name='Телефон'
    )
    email = models.CharField(
        max_length=255,
        blank=True,
        default='',
        verbose_name='Email'
    )

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='Учреждение', null=True)

    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен',
    )




