from django.shortcuts import render
from .forms import ContactForm

def home_view(request):
    return render(request, 'main_app/home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Thank you for your message! We will get back to you soon."
            return render(request, 'main_app/contact.html', {'form': form, 'success_message': success_message})
    else:
        form = ContactForm()
    return render(request, 'main_app/contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'main_app/contact_success.html')


