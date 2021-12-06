from django.contrib.auth.models import AbstractBaseUser, AbstractUser, UserManager, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
from django.utils import timezone
from morfis_core.morfis_models.hospital import Hospital
from .managers import MorfisUserManager


class Position(models.Model):
    title = models.CharField(
        max_length=255,
        unique = True,
        verbose_name='Название должности'
    )

    class Meta:
        verbose_name='Должность'
        verbose_name_plural='Должности'
        permissions = []


# class MorfisUser(AbstractUser):
class MorfisUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        verbose_name='Логин'
    )

    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Имя'
    )
    middle_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Отчество'
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Фамилия'
    )

    is_staff = models.BooleanField(
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
        verbose_name='Служебный',
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
        verbose_name='Активен',
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name ='Филиал', null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = MorfisUserManager()

    # objects = UserManager()

    # ФИО
    # Должность(ForeingKey)
    # Филиал(ForeingKey)
    # настройки
    # рабочего
    # стола
    def __str__(self):
        return self.username

    def is_admin(self):
        return self.is_staff and self.is_active

    class Meta:
        verbose_name = 'Морфис аккаунт'
        verbose_name_plural = 'Морфис аккаунты'