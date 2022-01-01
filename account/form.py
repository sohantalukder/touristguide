from django import forms
from .models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth import password_validation

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'input-box','placeholder': 'Username'})
    )

    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'class': 'input-box','placeholder': 'Password'})
    )

class SignupForm(UserCreationForm):
    name = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'input-box','placeholder': 'Name'})
    )
    username = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'input-box','placeholder': 'Username'})
    )

    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'input-box','placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'input-box','placeholder': 'Confirm Password'}),
        help_text=_("Enter the same password as before, for verification."),
    )
    email = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'input-box','placeholder': 'Email'})
    )
    contact_number = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'input-box','placeholder': 'Contact Namber'})
    )
    favt_food = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'fvt-items','placeholder': 'Favt. Food'})
    )
    favt_place = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'fvt-items','placeholder': 'Favt. Place'})
    )
    class Meta:
        model = User
        fields = ['name','username','email','contact_number','favt_food','favt_place','password1', 'password2']


class AccountPasswordchangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True,'class': 'input-box','placeholder': 'Old password'}),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'input-box','placeholder': 'New password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'input-box','placeholder': 'New confirmation password'}),
    )


class AccountPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email','class': 'input-box','placeholder': 'Email'})
    )


class AccountsetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New password"),strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'input-box','placeholder': 'Password'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"),strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'input-box','placeholder': 'Confirm Password'})
)
