from django.shortcuts import render, redirect
from .models import Home

def add_home(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        location = request.POST['location']
        size = request.POST['size']
        bedrooms = request.POST['bedrooms']
        bathrooms = request.POST['bathrooms']
        img = request.FILES['img']

        new_home = Home(
            title=title,
            description=description,
            price=price,
            location=location,
            size=size,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            img=img
        )
        new_home.save()
        return redirect('homes:home_list_view')  # Adjust to your URL name

    return render(request, 'homes/add_home.html')


def home_list(request):
    homes = Home.objects.all()  # Fetch all home objects
    return render(request, 'homes/home_list.html', {'homes': homes})

