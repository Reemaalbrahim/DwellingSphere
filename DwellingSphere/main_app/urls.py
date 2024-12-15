from . import views
from django.urls import path

app_name = "main_app"

urlpatterns = [
    path('', views.home_view, name='home_view'),  # Home page
    path('contact/', views.contact_view, name='contact_view'),
    path('contact/success/', views.contact_success_view, name='contact_success_view'),
    path('signin/', views.signin_view, name='signin_view'),  # Sign In page
    path('signup/', views.signup_view, name='signup_view'),  # Sign Up page
]
