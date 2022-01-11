from django.db import models

from .hospital import Hospital
from .utils import CommonInfo
from .organization import Organization
from datetime import datetime


class IcdCode(models.Model):
    code = models.CharField(max_length=255, verbose_name='Код диагноза')
    disease_description = models.CharField(max_length=255, verbose_name='Описание диагнозa')
    parent_code = models.CharField(max_length=255, verbose_name='Код родителя')

    # @property
    # def highlight(self, search):
    #     text = '%s (%s) %s' % (self.code, self.parent_code, self.disease_description)
    #     highlighted = text.replace(search, '<span class="highlight">{}</span>'.format(search))
    #     return highlighted


    def __str__(self):
        return '%s - %s' % (self.code, self.disease_description)

    class Meta:
        ordering=['pk',]
        verbose_name='Код международной классификации болезней'
        verbose_name_plural='Коды международной классификации болезней'




class Case(CommonInfo):

    class CaseStatus(models.TextChoices):
        OPEN = 'OPEN', 'Создана'
        SENDED = 'SENDED', 'Направлена'
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

    timestamp = models.DateTimeField(verbose_name='Дата направления')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name='Организация', null=True)
    disease_description = models.TextField(verbose_name='Диагноз заболевания (состояния)')
    mkb_code = models.ForeignKey(IcdCode, on_delete=models.CASCADE, verbose_name='Код МКБ')
    order_task = models.TextField(verbose_name='Задача исследования')

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name='Филиал', null=True)



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
        return 'Случай от %s #%s' % (self.timestamp.strftime("%d/%m/%y %H:%M"), self.get_request_id())

    class Meta:
        verbose_name = 'Случай'
        verbose_name_plural = 'Случаи'


class PreviousCase(models.Model):
    organization = models.CharField(max_length=255, verbose_name='Организация, давшая заключение')
    case = models.ForeignKey(Case, on_delete=models.CASCADE, verbose_name='Организация, давшая заключение')
    timestamp = models.DateTimeField(verbose_name='Дата заключения')
    request_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Регистрационный номер заключения'
    )
    conclusion = models.TextField(verbose_name='Заключение')