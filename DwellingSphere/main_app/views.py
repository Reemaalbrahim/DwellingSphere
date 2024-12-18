from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
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
            messages.success(request, "You have successfully signed in!")
            return redirect('main_app:home_view')  # Redirect to home after successful login
        else:
            messages.error(request, "Invalid username or password. You must register if you don't have an account.")
    
    return render(request, 'main_app/sign_in.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        role = request.POST['role']  # Get the user role

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.profile.role = role  # Assuming you have a Profile model linked to User
                user.save()
                messages.success(request, "Account created successfully! You can now sign in.")
                return redirect('main_app:signin_view')
            except Exception:
                messages.error(request, "Username already exists.")
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, 'main_app/sign_up.html')



def logout_view(request):
    logout(request)
    return redirect('main_app:home_view')  # Redirect to home or any other page




