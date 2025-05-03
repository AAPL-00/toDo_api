from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serilizers import UserSerializer
from .models import CustomUser

class CreateUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
