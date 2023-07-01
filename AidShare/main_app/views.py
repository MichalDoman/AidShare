from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

from main_app.models import Donation, Institution, Category
from main_app.forms import RegisterForm


class HomeView(ListView):
    """Landing page view of the app."""
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


class AddDonationView(TemplateView):
    """A ListView for institutions used for adding-donation form."""
    template_name = "form.html"

    def get_context_data(self, **kwargs):
        """Add all categories and institutions objects to the context."""
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all()
        institutions = Institution.objects.all()

        context["categories"] = categories
        context["institutions"] = institutions

        return context

    def post(self, request):
        if "categories" in request.POST:
            selected_categories = request.POST.getlist("categories")



class ModifiedLoginView(LoginView):
    def form_valid(self, form):
        pass


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
