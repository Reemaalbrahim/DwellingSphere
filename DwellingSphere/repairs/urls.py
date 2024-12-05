from . import views
from django.urls import path

app_name = "repairs"

urlpatterns = [
    path('', views.repair_list_view, name='repair_list_view'),
    path('<int:repair_id>/',views.repair_detail_view, name='repair_detail_view'),
]
