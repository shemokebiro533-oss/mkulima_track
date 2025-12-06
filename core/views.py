from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def home(request):
    """Home page view"""
    return render(request, 'core/index.html')

def about(request):
    """About page view"""
    return render(request, 'core/about.html')

def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        messages.success(request, f'Thank you {name}! We will contact you at {email} soon.')
        return redirect('contact')
    
    return render(request, 'core/contact.html')

def register(request):
    """User registration view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            login(request, user)
            messages.success(request, f'Welcome {username}! Registration successful.')
            return redirect('dashboard')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
    
    return render(request, 'core/register.html')

@login_required
def dashboard(request):
    """User dashboard view"""
    return render(request, 'core/dashboard.html')

@login_required
def profile(request):
    """User profile view"""
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    
    return render(request, 'core/profile.html')

def weather_forecast(request):
    """Weather forecast page"""
    forecast_data = [
        {'day': 'Today', 'temp': 28, 'condition': 'Sunny', 'icon': '☀️', 'advice': 'Good for planting'},
        {'day': 'Tomorrow', 'temp': 26, 'condition': 'Partly Cloudy', 'icon': '⛅', 'advice': 'Moderate planting'},
        {'day': 'Day 3', 'temp': 24, 'condition': 'Light Rain', 'icon': '🌧️', 'advice': 'Good for watering'},
        {'day': 'Day 4', 'temp': 27, 'condition': 'Sunny', 'icon': '☀️', 'advice': 'Excellent for planting'},
    ]
    
    return render(request, 'core/weather.html', {
        'forecast_data': forecast_data
    })