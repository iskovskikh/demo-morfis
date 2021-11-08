from django.db import models
from morfis_core.morfis_models.address import Address
from morfis_core.morfis_models.department import Department


class AbstractHospital(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название ЛПУ'
    )

    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        verbose_name='Адресс ЛПУ',
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

    class Meta:
        abstract = True


class Subsidiary(AbstractHospital):
    pass

class Hospital(AbstractHospital):

    subsidiary = models.ForeignKey(
        Subsidiary,
        on_delete=models.CASCADE,
        verbose_name='Филиалы',
        blank=True,
        null=True,
        default=None
    )
