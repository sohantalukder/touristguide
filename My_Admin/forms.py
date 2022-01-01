from django import forms
from places.models import *
from tourist.models import guider,hireguider

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = "__all__"


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = "__all__"


class TopratedplaceForm(forms.ModelForm):
    class Meta:
        model=Topratedplace
        fields="__all__"


class Sub_DistrictForm(forms.ModelForm):
    class Meta:
        model=Sub_District
        fields="__all__"


class TouristPlaceForm(forms.ModelForm):
    class Meta:
        model=TouristPlaces
        fields="__all__"

class PlaceorderForm(forms.ModelForm):
    class Meta:
        model=Placeorder
        fields="__all__"


class TopratedPlaceorderForm(forms.ModelForm):
    class Meta:
        model=TopPlaceorder
        fields="__all__"


class HotelForms(forms.ModelForm):
    class Meta:
        model=Hotels
        fields="__all__"


class FamousFoodForms(forms.ModelForm):
    class Meta:
        model=FamousFood
        fields="__all__"


class NearestPlaceForms(forms.ModelForm):
    class Meta:
        model=NearestPlace
        fields="__all__"


class guiderForm(forms.ModelForm):
    class Meta:
        model=guider
        fields="__all__"


class hireguiderForm(forms.ModelForm):
    class Meta:
        model = hireguider
        fields = "__all__"
