from django.db import models

class Department(models.Model):
    title = models.CharField(max_length=255, verbose_name='Отделение')
