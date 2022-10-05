from rest_framework import serializers

from .models import Tracker
from django.contrib.auth.models import User

class TrackerSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Tracker
        fields = ['price','time']

class RegistartionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password',]
        

