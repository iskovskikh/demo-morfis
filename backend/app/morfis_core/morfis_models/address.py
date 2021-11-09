from django.db import models


class Address(models.Model):
    address = models.CharField(max_length=255, blank=True, verbose_name='Адрес')
    # street = models.CharField(max_length=255, blank=True, verbose_name='Улица')
    # building = models.CharField(max_length=255, blank=True, verbose_name='Номер дома')
    # suite = models.CharField(max_length=255, blank=True, verbose_name='Корпус или строение')
    # region = models.CharField(max_length=255, blank=True, verbose_name='Район')
    # district = models.CharField(max_length=255, blank=True, verbose_name='Область')
    # city = models.CharField(max_length=255, blank=True, verbose_name='Город')
    # country = models.CharField(max_length=255, blank=True, verbose_name='Страна')
    # zip_code = models.CharField(max_length=255, blank=True, verbose_name='Почтовый индекс')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
