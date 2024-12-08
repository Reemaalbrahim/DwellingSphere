from django.urls import path
from . import views

app_name = 'designers'  # Namespace for the app

urlpatterns = [
    path('add/', views.add_designer_view, name='add_designer_view'),  # URL for adding a new designer
    path('list/', views.designers_list_view, name='designers_list_view'),  # URL for viewing the list of designers
]

