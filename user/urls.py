from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import CreateUserView, ChangePasswordView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]
