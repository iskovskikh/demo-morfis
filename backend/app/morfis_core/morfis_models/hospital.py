from django.db import models

from morfis_core.morfis_models.address import Address


class Hospital(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название учереждения'
    )


    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        verbose_name='Адресс учереждения',
        blank=True,
        null=True,
        default=None
    )


    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = 'Учереждение'
        verbose_name_plural = 'Учереждения'
