#django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


#self made
from .forms import UserRegistrationForm, UserLoginForm, ChangeUserData
from .models import Account


# Create your views here.

def register(request):                                                                
    form = UserRegistrationForm()                                                     
    context = {'form':form}                                                      
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        email = request.POST.get('email').lower()
        raw_password = request.POST.get('password1')
        username = request.POST.get('username').lower()
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            messages.success(request, f'Zarejestrowano pomyślnie, witaj {account.username}')
            login(request, account)
            return redirect('home') 
        else:
            if Account.objects.filter(username=username).exists():
                messages.error(request, 'Nazwa użytkownika jest zajęta, proszę wybrać inną')
            if Account.objects.filter(email=email).exists():
                messages.error(request, "Podany adres email jest już zajęty")
            messages.error(request, f'Wprowadzone hasła są różne')                                 #build in password checker try to give user message about their mistake
            return redirect('register')
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


def user_account_manage(request):
    if request.method == "POST":
        user_model = Account.objects.get(id=request.user.id)
        print(request.POST.get("end_of_travel"), '----------------------------------------------------------------------')
        if request.POST.get("end_of_travel"):
            user_model.delete()
            messages.success(request, "Dziękujemy za używanie naszego portalu, twoje konto zostało pomyślnie usunię.")
            return redirect('home')
        else:
            username = request.POST.get("username")
            if username != "":
                user_model.username = username

            email = request.POST.get("new_email")
            if email != "":
                user_model.email = email
                
            show_email = request.POST.get("show_email")
            if show_email == "on":
                user_model.hide_email = False
            user_model.save()
    form = ChangeUserData(request.POST, instance=Account)
    context = {'form': form}
    return render(request, 'core/user_account_manage.html', context)





