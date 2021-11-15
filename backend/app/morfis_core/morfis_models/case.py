from django.db import models
from .utils import CommonInfoMixin
from datetime import datetime


class ICDcode(models.Model):
    code = models.CharField(max_length=255, verbose_name='Код диагноза')
    disease_description = models.CharField(max_length=255, verbose_name='Название диагнозa')
    parent_code = models.CharField(max_length=255, verbose_name='Код родителя')

    def __str__(self):
        return '%s - %s' % (self.code, self.disease_description)

    class Meta:
        ordering=['pk',]
        verbose_name='Код международной классификации болезней'
        verbose_name_plural='Коды международной классификации болезней'

class Case(CommonInfoMixin):

    class CaseStatus(models.TextChoices):
        OPEN = 'OPEN', 'Создана'
        SENDED = 'SENDSD', 'Направлена'
        ACCEPTED = 'ACCEPTED', 'Принята'
        # ...
        ARCHIVED = 'ARCHIVED', 'Архивирована'
        CLOSE = 'CLOSE', 'Выполнена'

    status = models.CharField(
        max_length=10,
        choices=CaseStatus.choices,
        default=CaseStatus.OPEN,
    )

    request_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Регистрационный номер случая'
    )

    request_timestamp = models.DateTimeField(verbose_name='Дата направления')
    organization = models.CharField(max_length=255, verbose_name='Организация, создавшая направление')
    disease_description = models.TextField(verbose_name='Диагноз заболевания (состояния)')
    mkb_code = models.ForeignKey(ICDcode, on_delete=models.CASCADE, verbose_name='Код МКБ')
    order_task = models.TextField(verbose_name='Задача исследования')




    # pacient ForeingKey
    # bio-material List
    # Дата направления
    # Организация, создавшая направление
    # Диагноз заболевания(состояние)
    # Код МКБ(ForeingKey)
    # Задача исследования
    # Доп.клинические сведения
    # Результаты предыдущих исследований

    def get_request_id(self):
        request_id = None
        return self.request_id if self.request_id else '{номер не присвоен}'

    def __str__(self):
        return 'Случай от %s #%s' % (self.request_timestamp.strftime("%d/%m/%y %H:%M"), self.get_request_id())

    class Meta:
        verbose_name = 'Случай'
        verbose_name_plural = 'Случаи'
