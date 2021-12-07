from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home),
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
]