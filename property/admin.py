from django.contrib import admin

from .models import Flat
from .models import Complaint
from .models import Owner

class FlatAdmin(admin.ModelAdmin):
    search_fields = (
        'town',
        'address',
        'owner')
    readonly_fields = ["created_at"]
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'owners_phonenumber',
        'owner_pure_phone'
    )
    list_editable = ['new_building']
    raw_id_fields = ('liked_by',)
    list_filter = ['new_building', 'rooms_number', 'has_balcony']

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
