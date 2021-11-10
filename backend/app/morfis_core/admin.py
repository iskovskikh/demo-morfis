from django.contrib import admin
from .morfis_models.address import Address
from .morfis_models.hospital import Hospital, Subdivision
from .morfis_models.order import Order
from .morfis_models.utils import CommonInfoAdminMixin
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

@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    pass

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    pass
    # fields = ('title','address','departaments', 'subsidiaries')
    # inlines = [
    #     SubsidiaryInline,
    # ]

@admin.register(Order)
class OrderAdmin(CommonInfoAdminMixin):
    readonly_fields = ('status',)
    # pass

