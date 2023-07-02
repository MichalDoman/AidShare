from django import forms
from main_app.models import Donation


class AddDonationForm(forms.ModelForm):

    class Meta:
        model = Donation
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['name'] = 'bags'
        self.fields['zip_code'].widget.attrs['name'] = 'postcode'
        self.fields['pick_up_date'].widget.attrs['name'] = 'date'
        self.fields['pick_up_time'].widget.attrs['name'] = 'time'
        self.fields['pick_up_comment'].widget.attrs['name'] = 'more_info'


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Name"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Surname"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password_2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password_2"}))
