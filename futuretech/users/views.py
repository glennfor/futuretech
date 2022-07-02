import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, UserSignUpForm
from core.models import RegisteredUser

COURSE_REG_FEE = os.environ.get('COURSE_FEE') or 10_000

def register(request):
    template = 'register.html'
    register_form = RegistrationForm()
    if not request.user.is_authenticated:
        return redirect('/accounts/signup')

    this_user_registered = RegisteredUser.objects.filter(user = request.user)
    
    if this_user_registered:
        return redirect('/user/profile')

    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            first_name   = register_form.cleaned_data["first_name"] 
            middle_name  = register_form.cleaned_data["middle_name"] 
            last_name    = register_form.cleaned_data["last_name"] 
            birth_date   = register_form.cleaned_data["birth_date"] 
            gender       = register_form.cleaned_data["gender"] 
            email        = register_form.cleaned_data["email"] 
            phone_number = register_form.cleaned_data["phone_number"] 
            courses      = list(filter(lambda s : bool(s), request.POST.getlist('courses')))
            _course_count= len(courses) 
            _fee = COURSE_REG_FEE if _course_count <= 1 else (COURSE_REG_FEE + \
                    (COURSE_REG_FEE * (_course_count - 1))/2)
            
            amount = 'FCFA {}'.format(_fee)

            print(first_name, courses, birth_date, gender, phone_number)
            registereduser = RegisteredUser(
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                birth_date=birth_date,
                gender=gender,
                email=email,
                phone_number=phone_number,
                courses= '\n'.join(courses),
                user=request.user,
                registration_fee= amount,
                registration_status=None,
            )
            
            registereduser.save()
            return redirect('/user/profile')
    
    context = {
        'form': register_form,
    }
    return render(request, template, context)


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

   