from django.shortcuts import render, redirect
from .models import Designer

def add_designer_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        bio = request.POST['bio']
        contact_info = request.POST['contact_info']
        img = request.FILES.get('img')

        new_designer = Designer(
            name=name,
            bio=bio,
            contact_info=contact_info,
            img=img
        )
        new_designer.save()
        return redirect('designers:designers_list_view')  # Adjust to your URL name

    return render(request, 'designers/add_designer.html')


def designers_list_view(request):
    designers = Designer.objects.all()  # Fetch all designer objects
    return render(request, 'designers/designer_list.html', {'designers': designers})

