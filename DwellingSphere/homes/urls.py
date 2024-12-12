from django.urls import path
from . import views

app_name = 'homes'  # Namespace for the app

urlpatterns = [
    path('add/', views.add_home, name='add_home'),  # URL for adding a new home
    path('list/', views.home_list, name='home_list'),  # URL for viewing the list of homes
    path('detail/<home_id>/', views.home_detail, name='home_detail'),
]


