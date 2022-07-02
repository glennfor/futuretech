from django.shortcuts import render
from django.http import HttpResponse
from .models import RegisteredUser
# Create your views here.

def index(request):
    return render(request, 'index.html')

def show_profile(request):
    template = 'profile.html'
    if not request.user.is_authenticated:
        return redirect('/accounts/signup')
    
    registereduser = RegisteredUser.objects.filter(user = request.user)

    if not registereduser:
        return redirect(request, '')

    context = {
        'registereduser':registereduser
    }
    return render(request, template, context) 