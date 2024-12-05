from django.shortcuts import render
from .models import FurnitureShop

def shop_list_view(request):
    shops = FurnitureShop.objects.all()
    return render(request, 'furniture/shop_list.html', {'shops': shops})

def shop_detail_view(request, shop_id):
    shop = FurnitureShop.objects.get(id=shop_id)
    return render(request, 'furniture/shop_detail.html', {'shop': shop})
