from django.db import models
from django.contrib import admin


class CommonInfoMixin(models.Model):
    add_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    mod_date = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата изменения')


class CommonInfoAdminMixin(admin.ModelAdmin):
    readonly_fields = (
        'add_date',
        'mod_date',
    )
