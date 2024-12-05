from django.shortcuts import render
from .models import RepairService

def repair_list_view(request):
    repairs = RepairService.objects.all()
    return render(request, 'repairs/repair_list.html', {'repairs': repairs})

def repair_detail_view(request, repair_id):
    repair = RepairService.objects.get(id=repair_id)
    return render(request, 'repairs/repair_detail.html', {'repair': repair})

