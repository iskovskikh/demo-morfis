from django.db import models

from morfis_core.morfis_models.address import Address


class Organization(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название организации'
    )


    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        verbose_name='Адрес организации',
        blank=True,
        null=True,
        default=None
    )


    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
