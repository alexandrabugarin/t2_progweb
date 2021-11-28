from .models import *
from rest_framework import serializers

class PublicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacoes
        fields = '__all__'