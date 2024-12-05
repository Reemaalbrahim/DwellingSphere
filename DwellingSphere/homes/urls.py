from . import views
from django.urls import path

app_name = "homes"

urlpatterns = [
    path('', views.home_list_view, name='home_list_view'),
    path('<int:home_id>/', views.home_detail_view, name='home_detail_view'),
]