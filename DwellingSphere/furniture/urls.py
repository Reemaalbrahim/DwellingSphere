from django.urls import path
from . import views

app_name = 'furniture'  # Namespace for the app

urlpatterns = [
    path('add/', views.add_shop_view, name='add_shop_view'),  # URL for adding a new furniture shop
    path('list/', views.shop_list_view, name='shop_list_view'),  # URL for viewing the list of furniture shops
]

