from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

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


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")
