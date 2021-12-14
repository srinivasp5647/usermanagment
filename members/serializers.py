from rest_framework import fields, serializers
from django.contrib.auth.models import User
from .models import UserProfile
from .views import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="userprofiles-detail", lookup_field='name')
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'usernameasemail', 'username']



