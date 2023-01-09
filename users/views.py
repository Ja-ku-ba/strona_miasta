import os, shutil

#django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


#self made
from .forms import UserRegistrationForm, UserLoginForm, ChangeUserData
from .models import Account
from places.models import Locals, LocalProducts
from posts.models import Post

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

def remove_img(path, img_name):
    if os.path.exists(path + '/' + img_name) is False:
        # file did not exists
        return False
    os.remove(path + '/' + img_name)
    return True

def user_account_manage(request):
    if request.method == "POST":
        user_model = Account.objects.get(id=request.user.id)
        print(request.POST.get("end_of_travel"), '----------------------------------------------------------------------')
        if request.POST.get("end_of_travel"):
            user_profile_image_path = f'users/static/users/user_profile_pictures/{request.user.id}/'                             #delete proflie picture
            if os.path.exists(user_profile_image_path) is True:
                shutil.rmtree(user_profile_image_path)          
            try:
                local = Locals.objects.get(owner=request.user.id)                                                                #delete local images, where user was an owner
                path = f"C:/Users/jakub/Desktop/strona_miasta/places/static/locals/{local.id}"
                if os.path.exists(path) is True:
                    shutil.rmtree(path)   
            except:
                pass

            try:
                user_posts_static_folder = f"C:/Users/jakub/Desktop/strona_miasta/posts/static/posts/{request.user.id}"
                if os.path.exists(user_posts_static_folder) is True:
                    shutil.rmtree(user_posts_static_folder)   
            except:
                pass
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
    return render(request, 'users/user_account_manage.html', context)

def password_cahnge(request):
    form = PasswordChangeForm(user = request.user, data = request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # <-- keep the user loged after password change
            messages.success(request, 'Twoje hasło zostało zmienione pomyślnie.')
            return redirect('user_account_manage')
        else:
            messages.info(request, "Coś poszło nie tak, sprawdź poprawność wpisywanych haseł. Nie używaj haseł, które można łatwo odgadnąć")
    return render(request, "users/change_password.html")

