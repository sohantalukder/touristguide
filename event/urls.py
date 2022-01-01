from django.urls import path
from .views import TouristEventView,event_profile_view,event_requriement,payment,payment_status,edit_profile_view,\
    payment_complete,completepurchase,event_status

urlpatterns = [
path('create-event/',TouristEventView,name='create-event'),
path('profile/',event_profile_view,name='profile'),
path('event-status/<int:id>',event_status,name='event_status'),
path('edit-profile/',edit_profile_view,name='edit_profile'),
path('event-requriement/<int:id>',event_requriement,name='event-requriementfile'),
path('event-payment/<int:id>', payment,name='event_payment'),
path('payment-complete', payment_complete,name='payment_complete'),
path('complete-purchased/<val_id>/<tran_id>/', completepurchase, name="completepurchase"),
path('status/', payment_status,name='payment_status')
]