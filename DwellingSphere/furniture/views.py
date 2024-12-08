from django.shortcuts import render, redirect
from .models import FurnitureShop

def add_shop_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        contact_info = request.POST['contact_info']
        img = request.FILES.get('img')

        new_shop = FurnitureShop(
            name=name,
            description=description,
            contact_info=contact_info,
            img=img
        )
        new_shop.save()
        return redirect('furniture:shop_list_view')  # Adjust to your URL name

    return render(request, 'furniture/add_shop.html')


def shop_list_view(request):
    shops = FurnitureShop.objects.all()  # Fetch all furniture shop objects
    return render(request, 'furniture/shop_list.html', {'shops': shops})

