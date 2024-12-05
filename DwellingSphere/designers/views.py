from django.shortcuts import render
from .models import Designer

def designer_list_view(request):
    designers = Designer.objects.all()
    return render(request, 'designers/designer_list.html', {'designers': designers})

def designer_detail_view(request, designer_id):
    designer = Designer.objects.get(id=designer_id)
    return render(request, 'designers/designer_detail.html', {'designer': designer})

