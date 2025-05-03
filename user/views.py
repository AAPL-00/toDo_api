from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serilizers import UserSerializer, ChangePasswordSerializer
from .models import CustomUser

class CreateUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user
