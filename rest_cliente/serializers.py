from rest_framework import serializers
from manada.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['rut','nombre','gmail','telefono','direccion','usuario']

class DemoSumaSerializer(serializers.Serializer):
    a = serializers.IntegerField(help_text="Primer número", min_value=0, max_value=1000)
    b = serializers.IntegerField(help_text="Segundo número", min_value=0, max_value=1000)

class DemoSumaResultadoSerializer(serializers.Serializer):
    resultado = serializers.IntegerField(help_text="Suma de a + b")

class DemoSaludoSerializer(serializers.Serializer):
    mensaje = serializers.CharField(help_text="Saludo generado para el nombre indicado")
    fecha = serializers.DateTimeField(help_text="Fecha y hora del servidor")