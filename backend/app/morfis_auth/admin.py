from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from morfis_auth.forms import MorfisUserCreationForm, MorfisUserChangeForm
from morfis_auth.models import MorfisUser


@admin.register(MorfisUser)
class MorfisUserAdmin(UserAdmin):
    add_form = MorfisUserCreationForm
    form = MorfisUserChangeForm
    model = MorfisUser
    list_display = ('username', 'is_staff', 'is_active',)
    list_filter = ('username', 'last_name', 'first_name', 'middle_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'last_name', 'first_name', 'middle_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'username','last_name', 'first_name', 'middle_name',  'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)

