from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main_app.views import HomeView, AddDonationView, FormConfirmationView, LoginView, RegisterView, ProfileView, \
    ProfileUpdateView

urlpatterns = [
                  path('', include("main_app.urls")),
                  path('admin/', admin.site.urls),
                  path("accounts/", include(("django.contrib.auth.urls", 'auth'), namespace='auth')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
