from typing import Any
from urllib.request import Request

from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from provedor.api.v1.serializers import LeadSerializer, ProvedorSerializer
from provedor.models import Lead, Provedor


class ProvedorView(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ProvedorSerializer
    permission_classes = [IsAuthenticated]
    queryset = Provedor.objects.all()


class LeadView(ListModelMixin, CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]
    # queryset = Lead.objects.all()

    def get_queryset(self):
        cpf_cnpj_indicador = self.request.query_params.get("indicador", None)
        return Lead.objects.filter(cpf_cnpj_indicador=cpf_cnpj_indicador)

    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        cpf_cnpj_indicador = self.request.query_params.get("indicador", None)
        if cpf_cnpj_indicador is None:
            return Response({"mensagen": "Query Parameter indicador obrigatorio"}, status=status.HTTP_400_BAD_REQUEST)
        return super().list(request, *args, **kwargs)
