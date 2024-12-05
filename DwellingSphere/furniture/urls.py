from . import views
from django.urls import path

app_name = "furniture"

urlpatterns = [
    path('', views.shop_list_view, name='shop_list_view'),
    path('<int:shop_id>/', views.shop_detail_view, name='shop_detail_view'),
]
