from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RegisteredUser
# Create your views here.

def index(request):
    return render(request, 'index.html')

def show_profile(request):
    template = 'profile.html'
    if not request.user.is_authenticated:
        return redirect('/accounts/signup')
    
    if not RegisteredUser.objects.filter(user = request.user).exists():
        return redirect('/register')
        
    registereduser = RegisteredUser.objects.get(user = request.user)

    print(registereduser)
    context = {
        'registereduser':registereduser,
    }
    return render(request, template, context) 