from rest_framework import serializers
from .models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta():
        model = Empresa
        fields = (
            'cnpj',
            'name',
            'razao_social',
            'sede',
            'estado',
            'ranking'
        )
