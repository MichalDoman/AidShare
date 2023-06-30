from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Name"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Surname"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password_2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password_2"}))
