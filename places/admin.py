from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Division)
admin.site.register(District)
admin.site.register(Sub_District)
admin.site.register(Hotels)
admin.site.register(NearestPlace)
admin.site.register(FamousFood)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['place_name', 'division', 'district', 'sub_district']
admin.site.register(TouristPlaces, PlaceAdmin)

admin.site.register(Ratting)
admin.site.register(Placeorder)
admin.site.register(Topratedplace)
admin.site.register(TopPlaceorder)

