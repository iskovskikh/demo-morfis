from django.contrib import admin
from .morfis_models.address import Address
from .morfis_models.hospital import Hospital
from .morfis_models.case import Case, IcdCode
from .morfis_models.utils import CommonInfoAdminMixin
from .morfis_models.organization import Organization
# Register your models here.

from django.contrib import admin


# from django.core import urlresolvers
# from django.utils.html import format_html

# class SubsidiaryInline(admin.TabularInline):
#     model = Subsidiary
#     extra = 0

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    pass





@admin.register(Case)
class CaseAdmin(CommonInfoAdminMixin):
    # readonly_fields = ('add_date', 'mod_date')
    fields = None
    pass


@admin.register(IcdCode)
class ICDcodeAdmin(admin.ModelAdmin):
    pass


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass