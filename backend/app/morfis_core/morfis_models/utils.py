from django.db import models
from django.contrib import admin

from morfis_auth.models import MorfisUser
from morfis_core.middlewares import CurrentUserMiddleware

from datetime import datetime


class CommonInfo(models.Model):
    add_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    mod_date = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата изменения')

    created_by = models.ForeignKey(MorfisUser, on_delete=models.CASCADE, related_name='%(class)s_requests_created')
    lastmodified_by = models.ForeignKey(MorfisUser, on_delete=models.CASCADE,related_name='%(class)s_requests_modified')


    @staticmethod
    def get_current_user():
        return CurrentUserMiddleware.get_current_user()

    def set_user_fields(self, user):
        """
        Set user-related fields before saving the instance.
        If no user with a primary key is given the fields are not
        set.
        """
        if user and user.pk:
            if not self.pk:
                self.created_by = user
                # self.add_date = datetime.now()
            self.lastmodified_by = user

    def save(self, *args, **kwargs):
        # self.mod_date = datetime.now()
        current_user = self.get_current_user()
        self.set_user_fields(current_user)
        super(CommonInfo, self).save(*args, **kwargs)


class CommonInfoAdminMixin(admin.ModelAdmin):
    readonly_fields = (
        'add_date',
        'mod_date',
    )
