from django.urls import path
from . import views

app_name = 'repairs'  # Namespace for the app

urlpatterns = [
    path('add/', views.add_service_view, name='add_service_view'),  # URL for adding a new repair service
    path('list/', views.repair_list_view, name='repair_list_view'),  # URL for viewing the list of repair services
]

