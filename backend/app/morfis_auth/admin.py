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
    list_display = ('username','get_groups', 'is_active',)
    list_filter = ('username', 'last_name', 'first_name', 'middle_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
                'last_name',
                'first_name',
                'middle_name',
                'subdivision'
            )}),
        ('Permissions', {
            'fields': (
                'groups',
                'user_permissions',
                'is_staff',
                'is_active'
            )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'last_name',
                'first_name',
                'middle_name',
                'password1',
                'password2',
                'is_staff',
                'is_active',
                'subdivision'
            )}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)

    def get_groups(self, obj):
        return list(obj.groups.values_list('name', flat=True))

    get_groups.short_description = 'Группы'
