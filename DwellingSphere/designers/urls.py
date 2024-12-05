from . import views
from django.urls import path

app_name = "designers"

urlpatterns = [
    path('', views.designer_list_view, name='designer_list_view'),
    path('<int:designer_id>/', views.designer_detail_view, name='designer_detail_view'),
]
