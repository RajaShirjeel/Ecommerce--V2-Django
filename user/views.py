from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password, check_password
from .forms import SignupForm, LoginForm
from .models import User
# Create your views here.
def signup_user(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)

        if signup_form.is_valid():
           user = signup_form.save(commit=False)
           password = request.POST.get('password')
           user.password = make_password(password)
           user.save()
           login(request, user)
           return redirect('home:home')
        
    else:
        signup_form = SignupForm()
    
    return render(request, 'user/signup.html', {'form': signup_form})


def login_user(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()
        if user is not None:
           if check_password(password, user.password):
               login(request, user)
               return redirect('home:home')
           else:
               login_form.add_error('password', 'Incorrect password!')
        else:
            login_form.add_error('email', 'No user exists on the email please signup instead!')
    
    else:
        login_form = LoginForm()

    return render(request, 'user/login.html', {'form':login_form})