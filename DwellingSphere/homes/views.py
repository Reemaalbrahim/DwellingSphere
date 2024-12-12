from django.shortcuts import render, redirect
from .models import Home
from django.core.paginator import Paginator

def add_home(request):
    if request.method == 'POST':
        title = request.POST['title']  # This is the home type
        contact = request.POST['contact']
        price = request.POST['price']
        location = request.POST['location']
        size = request.POST['size']
        bedrooms = request.POST['bedrooms']
        bathrooms = request.POST['bathrooms']
        img = request.FILES['img']

        new_home = Home(
            title=title,
            contact=contact,
            price=price,
            location=location,
            size=size,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            img=img
        )
        new_home.save()
        return redirect('homes:home_list')  # Adjust to your URL name

    return render(request, 'homes/add_home.html')

def home_list(request):
    location = request.GET.get('location')
    title = request.GET.get('title')
    homes = Home.objects.all()

    if location:
        homes = homes.filter(location=location)
    if title:
        homes = homes.filter(title=title)

    # Implement pagination
    paginator = Paginator(homes, 9)  # Show 9 homes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'homes/home_list.html', {'page_obj': page_obj})

def home_detail(request, home_id:int):

    home= Home.objects.get(pk=home_id)

    return render(request, 'homes/home_detail.html', {'home': home})


