from rest_auth.views import LoginView as BaseLoginView
from rest_framework import status
from rest_framework.response import Response

from base.api.v1.serializers import LoginSerializer


class LoginView(BaseLoginView):
    serializer_class = LoginSerializer
    lookup_field = "uuid"

    def get_response(self):
        serializer_class = self.get_response_serializer()
        serializer = serializer_class(self.user)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
