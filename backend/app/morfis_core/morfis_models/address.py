from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255, blank=True, verbose_name='Улица')
    building = models.CharField(max_length=255, blank=True, verbose_name='Номер дома')
    suite = models.CharField(max_length=255, blank=True, verbose_name='корпус или строение')
    region = models.CharField(max_length=255, blank=True, verbose_name='Район')
    city = models.CharField(max_length=255, blank=True, verbose_name='Город')
    country = models.CharField(max_length=255, blank=True, verbose_name='Страна')
    zip_code = models.CharField(max_length=255, blank=True, verbose_name='Почтовый индекс')
