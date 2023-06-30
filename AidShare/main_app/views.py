from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView
from django.contrib.auth.models import User
from django import forms

from main_app.models import Donation, Institution


class HomeView(ListView):
    """Landing Page of the app."""
    model = Donation
    template_name = "donation_index.html"
    template_name_suffix = "_index"
    context_object_name = "donations"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        """Add institutions objects, number of bags and supported institutions count to the context."""
        context = super().get_context_data()
        user = self.request.user
        donations = Donation.objects.filter(user=user.id)
        institutions = Institution.objects.all()
        context['institutions'] = institutions

        sum_of_bags = 0
        for donation in donations:
            sum_of_bags += donation.quantity

        context['bags'] = sum_of_bags

        institutions_count = []
        for donation in donations:
            institutions.append(donation.institution)

        context['institutions_count'] = len(set(institutions_count))
        return context


class AddDonationView(View):
    def get(self, request):
        return render(request, "form.html")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Name"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Surname"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password_2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password_2"}))


class RegisterView(FormView):
    """A view that enables users to create accounts."""
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        """Check if registration conditions are met. If so create an account and redirect to LoginView.
        Otherwise, return invalid form error."""
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        password_2 = form.cleaned_data['password_2']

        if User.objects.filter(email=email).exists():
            form.add_error(None, 'This e-mail address is already taken!')
            return super().form_invalid(form)

        if password != password_2:
            form.add_error(None, 'Passwords did not match!')
            return super().form_invalid(form)

        User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        return super().form_valid(form)
