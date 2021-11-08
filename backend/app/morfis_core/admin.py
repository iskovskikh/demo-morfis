from django.contrib import admin
from .morfis_models.hospital import Hospital
# Register your models here.

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):

    
    pass