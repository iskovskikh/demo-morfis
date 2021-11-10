from django.db import models
from .utils import CommonInfoMixin


class Order(CommonInfoMixin):
    class OrderStatus(models.TextChoices):
        OPEN = 'OPEN', 'Создана'
        SENDED = 'SENDSD', 'Направлена'
        ACCEPTED = 'ACCEPTED', 'Принята'
        # ...
        ARCHIVED = 'ARCHIVED', 'Архивирована'
        CLOSE = 'CLOSE', 'Выполнена'

    status = models.CharField(
        max_length=10,
        choices=OrderStatus.choices,
        default=OrderStatus.OPEN,
    )

    id_number = models.CharField(max_length=255, blank=False, null=False, verbose_name='Регистрационный номер')

    #pacient ForeingKey
    #bio-material List

    def __str__(self):
        return 'Заявка #%s' % self.id_number

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'