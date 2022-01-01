from account.models import User
from .models import UserTouristEvent,AdminTouristEvent
from django import forms
from .models import Destination,TransportService

HIRE_GUIDE = {
    ('Yes', 'Yes'),
    ('No', 'No'),
}
class AdminTouristEventForm(forms.ModelForm):
    event_title  = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'input-box','placeholder': 'Event Title'})
    )
    event_description  = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'input-box','placeholder': 'Description'})
    )
    traveling_dates  = forms.DateField(
        widget= forms.NumberInput(attrs={'type': 'date','placeholder': 'dd/mm/yyyy'})
    )
    # total_traveling_person  = forms.CharField(
    #     widget= forms.TextInput(attrs={'placeholder': 'Person'})
    # )
    traveling_location  = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'select_location','placeholder': 'Traveling Location'})
    )
    event_price  = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'select_location','placeholder': 'Event Price'})
    )
    # traveller_destination  = forms.ModelChoiceField(
    #     queryset = Destination.objects.all(),
    #     widget= forms.Select(attrs={'class': 'select_location','placeholder': 'Destination'})
    # )
    guider_confirmation  = forms.ChoiceField(
        choices=HIRE_GUIDE,
        widget= forms.Select(attrs={'class': 'select_location'})
    )
    transport_service  = forms.ModelChoiceField(
        queryset = TransportService.objects.all(),
        widget= forms.Select(attrs={'class': 'select_location',})
    )

    class Meta:
        """Meta definition for UserTouristEventform."""

        model = AdminTouristEvent
        fields = '__all__'
        exclude = ('event_creator','slug','publish','create_at','updated_at',)

   


class ProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','contact_number','favt_food','favt_place']