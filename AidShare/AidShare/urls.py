from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main_app.views import HomeView, AddDonationView, FormConfirmationView, LoginView, RegisterView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', LoginView.as_view(), name="login"),
    path('', HomeView.as_view(), name="home"),
    path('add-donation/', AddDonationView.as_view(), name="add_donation"),
    path('form-confirmation/', FormConfirmationView.as_view(), name="form_confirmation"),
    path('register/', RegisterView.as_view(), name="register"),
    path('profile/', ProfileView.as_view(), name="profile")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
