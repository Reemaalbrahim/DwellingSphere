from django.shortcuts import render
from .models import Home

def home_list_view(request):
    homes = Home.objects.all()
    return render(request, 'homes/home_list.html', {'homes': homes})

def home_detail_view(request, home_id):
    home = Home.objects.get(id=home_id)
    return render(request, 'homes/home_detail.html', {'home': home})

def home_form_view(request):
    # Form handling logic will go here
    pass
