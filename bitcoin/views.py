from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
import requests
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import TrackerSerializer,RegistartionSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Tracker


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_live_price(request):
    url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
    response = requests.get(url).json()["data"]
    entry = Tracker.objects.create(price = float(response["amount"]))
    entry.save()
    data = {"btc_live_price": response["amount"],"currency":"USD"}
    return Response(data)

#
class PriceList(generics.ListAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
def register(request):
    serializer = RegistartionSerializer(data = request.data) 
    if serializer.is_valid(raise_exception=True):
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = User(username = username)
        data = {}
        user.set_password(password)
        user.save()
        token = Token.objects.get(user = user).key
        data['message'] = "User created successfully"
        data['token'] = token
        data['username'] = username
        return Response(data)
    
    else:
        return Response(serializer.errors)