from django.urls import path
from main_app.views import LoginView, HomeView, AddDonationView, FormConfirmationView, RegisterView, ProfileView, \
    ProfileUpdateView, GetInstitutions

urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('profile/<int:pk>/', ProfileView.as_view(), name="profile"),
    path('profile-update/<int:pk>/', ProfileUpdateView.as_view(), name="profile_update"),

    path('add-donation/', AddDonationView.as_view(), name="add_donation"),
    path('form-confirmation/', FormConfirmationView.as_view(), name="form_confirmation"),
    path('get-institutions/', GetInstitutions.as_view(), name="get_institutions"),
]
