from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _
from rest_auth.serializers import LoginSerializer as BaseLoginSerializer
from rest_auth.serializers import UserDetailsSerializer as BaseUserDetailsSerializer
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as BaseTokenObtainPairSerializer


class UserDetailsSerializer(BaseUserDetailsSerializer):
    class Meta:
        model = get_user_model()
        fields = ("pk", "username", "email", "name")
        read_only_fields = ("email",)


class TokenObtainPairSerializer(BaseTokenObtainPairSerializer):
    def to_representation(self, instance):
        refresh = self.get_token(instance)
        user_serializer = UserDetailsSerializer(instance)
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": user_serializer.data,
        }
        return data


class LoginSerializer(BaseLoginSerializer):
    def _validate_username_email(self, username, email, password):
        user = None

        if username and password:
            user = authenticate(username=username, password=password)
        elif email and password:
            user = authenticate(email=email, password=password)
        else:
            message = _('Must include either "username" or "email" and "password".')
            raise ValidationError(message)

        return user
