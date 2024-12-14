from django.shortcuts import render, redirect
from .models import RepairService

def add_service_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        contact_info = request.POST['contact_info']
        img = request.FILES.get('img')

        new_service = RepairService(
            name=name,
            description=description,
            contact_info=contact_info,
            img=img
        )
        new_service.save()
        return redirect('repairs:repair_list_view')  # Adjust to your URL name

    return render(request, 'repairs/add_service.html')


def repair_list_view(request):
    services = RepairService.objects.all()  # Fetch all repair service objects
    return render(request, 'repairs/repair_list.html', {'services': services})


