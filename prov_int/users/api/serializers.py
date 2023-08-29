from django.contrib.auth import get_user_model
from rest_framework import serializers

from prov_int.users.models import User as UserType

User = get_user_model()


class UserSerializer(serializers.ModelSerializer[UserType]):
    class Meta:
        model = User
        fields = ["uuid", "username", "name", "email", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "uuid"},
        }
