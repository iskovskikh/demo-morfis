from django.db import models
from django.db.models import UniqueConstraint, Q

from morfis_core.morfis_models.address import Address
from morfis_core.morfis_models.department import Department


class Hospital(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название ЛПУ'
    )

    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        verbose_name='Адресс ЛПУ',
        blank=True,
        null=True,
        default=None
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Учереждение'
        verbose_name_plural = 'Учереждения'


class Subdivision(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название филиала'
    )

    master_subdivision = models.BooleanField(default=False, verbose_name='Основное подразделение')

    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        verbose_name='Адресс филиала',
        blank=True,
        null=True,
        default=None
    )

    departaments = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name='Отделения',
        blank=True,
        null=True,
        default=None
    )

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        verbose_name='Основное учреждение',
        related_name='subsidiaries'
    )

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            UniqueConstraint(fields=['master_subdivision'], condition=Q(master_subdivision=True),
                             name='master_subdivision')
        ]

        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'
