from django.shortcuts import render, redirect
# from django.
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, UserSignUpForm
from core.models import RegisteredUser


# Create your views here.


def register(request):
    template = 'register.html'
    if not request.user.is_authenticated:
        return redirect('/accounts/signup')

    this_user_registered = RegisteredUser.objects.filter(user = request.user)
    
    if this_user_registered:
        return redirect('/user/profile')

    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():

            first_name   = register_form.cleaned_data["first_name"] 
            middle_name  = register_form.cleaned_data["first_name"] 
            last_name    = register_form.cleaned_data["first_name"] 

            birth_date   = register_form.cleaned_data["first_name"] 
            gender       = register_form.cleaned_data["first_name"] 

            email        = register_form.cleaned_data["first_name"] 

            phone_number = register_form.cleaned_data["first_name"] 

            course       = register_form.cleaned_data["first_name"] 

            register_user = RegisteredUser(
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                birth_date=birth_date,
                gender=gender,
                email=email,
                phone_number=phone_number,
                course=course,
                user=request.user
            )
            
            registereduser.save()
            return redirect('/user/profile')

    else:
        register_form = RegistrationForm()

    return render(request, template)


def signup(request):
    template = "signup.html"
    user_form = UserSignUpForm()
    if request.method == 'POST':
        user_form = UserSignUpForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=True)
            user.save()
            login(request, user)
            return redirect('/home')

    context = {
        'userform': user_form,
    }

    return render(request, template, context)

def signin(request):
    template_name = "login.html"
    context = {
        'error': None,
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        context['error'] = 'Wrong username and/or password!'    
        if user:
            context['error'] = 'This account has been disabled!'
            if user.is_active:
                login(request, user)
                return redirect('/') 
    
    return render(request, template_name, context)


def signout(request):
    logout(request)
    return redirect('/')

   