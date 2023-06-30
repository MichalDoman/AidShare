from django.contrib import admin
from django.urls import path, include

from main_app.views import HomeView, AddDonationView, ModifiedLoginView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/login/", ModifiedLoginView.as_view(), name="login"),
    path('', HomeView.as_view(), name="home"),
    path('add-donation/', AddDonationView.as_view(), name="add_donation"),
    path('register', RegisterView.as_view(), name="register"),
]
