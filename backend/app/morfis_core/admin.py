from django.contrib import admin
from .morfis_models.address import Address
from .morfis_models.hospital import Hospital, Subdivision
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

    # readonly_fields = ('subsidiaries_list')
    # fields = ('title', 'subsidiaries')
    #
    # def books_list(self, obj):
    #     subsidiaries = Subsidiary.objects.filter(hospital=obj)
    #     if subsidiaries.count() == 0:
    #         return '(None)'
    #     subsidiary_links = []
    #     for subsidiary in subsidiaries:
    #         change_url = urlresolvers.reverse('admin:myapp_subsidiary_change', args=(subsidiary.id,))
    #         subsidiary_links.append('<a href="%s">%s</a>' % (change_url, unicode(subsidiary))
    #     return format_html(', '.join(subsidiary_links))
    #
    # subsidiaries_list.allow_tags = True
    # subsidiaries_list.short_description = 'Book(s)'