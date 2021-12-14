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

# Rest API
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import UserProfile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Password auto-generate and encrypt
import random
import string
from cryptography.fernet import Fernet

#


@login_required(login_url='/management/login/')
def home(request):
    name = request.user.username
    return render(request, 'base.html', {'name': name})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('/management/')
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
            return redirect('/management/login')
        
    return render(request, 'register.html', {'form':form})


def logout(request):
    auth.logout(request)

    return render(request, 'login.html')



class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    lookup_field = 'name'
    serializer_class = UserSerializer

    def create(self, request):
        serializer_context = {
                        'request': request,
                    }
        serializer = UserSerializer(data=request.data, context = serializer_context)
        #pdb.set_trace()
        if serializer.is_valid():
            # serializer.save(commit=False)
            if serializer.validated_data['usernameasemail']:
                serializer.validated_data['username'] = serializer.validated_data['email']
                n = 10
                pas = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
                
                key = Fernet.generate_key()
                fernet = Fernet(key)
                enpass = fernet.encrypt(pas.encode())
                serializer.validated_data['password'] = enpass
                serializer.save()
            else:
                n = 10
                pas = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
                
                key = Fernet.generate_key()
                fernet = Fernet(key)
                enpass = fernet.encrypt(pas.encode())
                serializer.validated_data['password'] = enpass

                serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# @api_view(['POST'])
# def UserAdd(request):

#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         pdb.set_trace()


#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

