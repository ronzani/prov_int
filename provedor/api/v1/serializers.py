from rest_framework.serializers import ModelSerializer

from provedor.models import Provedor


class ProvedorSerializer(ModelSerializer):
    class Meta:
        model = Provedor
        exclude = ["created_at", "updated_at"]


class LeadSerializer(ModelSerializer):
    class Meta:
        model = Provedor
        exclude = ["created_at", "updated_at"]
