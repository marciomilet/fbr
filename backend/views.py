from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Empresa
from .serializers import EmpresaSerializer

class EmpresaAPIView(APIView):
    def get(self, request):
        empresa = Empresa.objects.all()
        serializer = EmpresaSerializer(empresa, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmpresaSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
        
# Create your views here.
