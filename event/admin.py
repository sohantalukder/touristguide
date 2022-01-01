from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(EventOrder)
@admin.register(AdminTouristEvent)
class AdminTouristEventAdmin(admin.ModelAdmin):

    list_display = ('event_title','event_creator','traveling_location','traveling_dates','publish','event_image')


@admin.register(UserTouristEvent)
class UserTouristEventAdmin(admin.ModelAdmin):

    list_display = ('event_creator','event_title','traveling_dates')


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):

    list_display = ('location_name',)


@admin.register(TransportService)
class TransportServiceAdmin(admin.ModelAdmin):

    list_display = ('transport_name',)

from .models import PaymentDetails
# Register your models here.

@admin.register(PaymentDetails)
class PaymentDetailsAdmin(admin.ModelAdmin):
    '''Admin View for PaymentDetails'''

    list_display = ('transaction_id','ammount','card_type','payment_status')

admin.site.register(EventInfo)

