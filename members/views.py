from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import RegistrationForm
# Create your views here
from django.contrib import messages
import pdb
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
    name = request.user.username
    return render(request, 'base.html', {'name': name})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/home/')
    return render(request, 'login.html')



def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            
            user = form.save()
            pw = user.password
            user.set_password(pw)
            user.save()
            return redirect('/login')
        
    return render(request, 'register.html', {'form':form})


def logout(request):
    auth.logout(request)

    return render(request, 'login.html')
