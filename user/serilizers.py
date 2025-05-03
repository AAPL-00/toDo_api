from rest_framework import serializers
from user.models import CustomUser
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        extra_kwargs = {
            'username': {'required': True, 'allow_blank': False},
        }

    def validate_password(self, value):
        validate_password(value, user=None)
        return value

    def create_user(self, validated_data):
        user = CustomUser.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password']
        )
        return user
