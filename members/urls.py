from django.urls import path, include
import rest_framework
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)


app_name = 'members'
urlpatterns = [
    path('', home),
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('', include(router.urls)),
    
    path('api-auth/', include('rest_framework.urls')),
    
]