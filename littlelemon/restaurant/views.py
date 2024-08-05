from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from .models import Menu, Booking
from .serializers import UserSerializer,MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permissionclass = [IsAuthenticated, IsAdminUser]
    queryset = User.objects.all()
    
class MenuItemView(generics.ListCreateAPIView):
    serializer_class = MenuSerializer
    permissionclass = [IsAuthenticated]
    queryset = Menu.objects.all()
    
class SingleMenuItemView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated] 
   