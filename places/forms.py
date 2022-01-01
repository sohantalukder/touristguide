from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from places.models import *


class OrderForm(forms.ModelForm):
    start_date=forms.DateField(widget=forms.SelectDateWidget)
    end_date=forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model=Placeorder
        fields=['start_date','end_date','person']

class TOpOrderForm(forms.ModelForm):
    start_date=forms.DateField(widget=forms.SelectDateWidget)
    end_date=forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model=TopPlaceorder
        fields=['start_date','end_date','person']