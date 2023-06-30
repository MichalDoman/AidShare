from django.contrib import admin
from django.urls import path

from main_app.views import HomeView, AddDonationView, LoginView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('add-donation/', AddDonationView.as_view(), name="add_donation"),
    path('login', LoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name="register"),
]
