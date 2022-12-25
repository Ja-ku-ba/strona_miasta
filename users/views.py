#django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


#self made
from .forms import UserRegistrationForm, UserLoginForm
from .models import Account


# Create your views here.

def register(request):                                                                      #email test@test.test, username test, password12 test: doe not return any response
    form = UserRegistrationForm()                                                           #email test@test.com, username test, pasword12 http://127.0.0.1:8000/konta/zarejestruj: works properly
    context = {'form':form}                                                                 #email test1@test1.test1, username test1, password12 http://127.0.0.1:8000/konta/zarejestruj: works properly
    if request.method == "POST":
        register_form = UserRegistrationForm(request.POST)
        email_lower = request.POST.get('email').lower()
        username_lower = request.POST.get('username').lower()
        password1 = request.POST.get('password1')                                           #plain password
        password2 = request.POST.get('password2')
        if Account.objects.filter(username=username_lower).exists():
            messages.error(request, 'Nazwa użytkownika jest zajęta, proszę wybrać inną')
        if Account.objects.filter(email=email_lower).exists():
            messages.error(request, "Podany adres email jest już zajęty")
        if password1 != password2:
            messages.error(request, "Podane hasła nie są identyczne")
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.username = username_lower
            user.email = email_lower
            user = register_form.save()
            login(request, user)
            messages.success(request, f'Zarejestrowano pomyślnie, witaj {user.username}')
            return redirect('home')
    return render(request, 'users/register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        status = True
        try:
            user = Account.objects.get(email=email)
        except:
            status = False
        user = authenticate(request, email=email, password=password)
        if (user is None) or (status is False):
            messages.info(request, 'Wprowadzono nieporawnie email lub hasło, spróbój jeszcze raz.')
        else:
            login(request, user)
            messages.success(request, f'Zalogowano pomyslnie, witaj {user.username}')
            return redirect('home')

    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')
