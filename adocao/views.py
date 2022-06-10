from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST,HTTP_200_OK
from .serializers import AdocaoSerializer
from .email_service import send_email_confirmation
from .models import Adocao


class AdocaoList(APIView):

    def get(self, request, format=None):
        adoptions = Adocao.objects.all()
        serializer = AdocaoSerializer(adoptions, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, format=None):
        serializer = AdocaoSerializer(data=request.data)
        if serializer.is_valid():
            adoption = serializer.save()
            send_email_confirmation(adoption)   
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "errors": serializer.errors,
                "message": "Houveram erros de validacao",
            },
            status=HTTP_400_BAD_REQUEST,
        )
