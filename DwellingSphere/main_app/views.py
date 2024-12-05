from django.shortcuts import render, redirect
from .forms import ContactForm

def home_view(request):
    return render(request, 'main_app/home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'main_app/contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'main_app/contact_success.html')

