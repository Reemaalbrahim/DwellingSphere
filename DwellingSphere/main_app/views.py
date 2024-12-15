from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
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

def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_app:home_view')  # Redirect to home after successful login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'main_app/sign_in.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Account created successfully! You can now sign in.")
                return redirect('main_app:signin_view')
            except:
                messages.error(request, "Username already exists.")
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'main_app/sign_up.html')



