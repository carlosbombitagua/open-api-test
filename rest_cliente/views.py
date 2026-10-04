from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from manada.models import Cliente
from django.utils import timezone
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse
from .serializers import (
    ClienteSerializer, DemoSaludoSerializer, DemoSumaSerializer, DemoSumaResultadoSerializer,
)

@extend_schema(
    methods=['GET'],
    responses=ClienteSerializer(many=True),
    summary='Lista los clientes',
)
@extend_schema(
    methods=['POST'],
    request=ClienteSerializer,
    responses={201: ClienteSerializer, 400: None},
    summary='Crea un cliente',
)
@csrf_exempt
@api_view(['GET','POST'])
def lista_clientes(request):
    if request.method == 'GET':
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=['Demo'],
    summary='Endpoint demo de saludo',
    description=(
        'Endpoint de prueba para verificar que la documentación OpenAPI se genera sola.\n\n'
        '## Qué hace\n'
        'Devuelve un saludo personalizado junto con la fecha y hora del servidor.\n\n'
        '## Reglas\n'
        '- El parámetro `nombre` es **opcional**; si se omite se usa `mundo`.\n'
        '- El nombre no puede superar los **50 caracteres**.\n'
        '- La fecha se devuelve en formato ISO 8601 (UTC).\n\n'
        '## Ejemplo de uso\n'
        '```\n'
        'GET /api/demo/saludo?nombre=Italo\n'
        '```\n\n'
        '> Este endpoint es solo de prueba y no accede a la base de datos.'
    ),
    parameters=[
        OpenApiParameter(
            'nombre', str, OpenApiParameter.QUERY,
            description='Nombre a saludar (máx. 50 caracteres)',
            default='mundo',
            examples=[
                OpenApiExample('Nombre simple', value='Italo'),
                OpenApiExample('Nombre compuesto', value='Ana María'),
            ],
        ),
    ],
    responses={
        200: OpenApiResponse(
            response=DemoSaludoSerializer,
            description='Saludo generado correctamente',
            examples=[
                OpenApiExample(
                    'Respuesta exitosa',
                    value={'mensaje': 'Hola Italo', 'fecha': '2026-10-04T22:40:25.686104Z'},
                ),
            ],
        ),
        400: OpenApiResponse(
            description='El nombre supera los 50 caracteres',
            examples=[
                OpenApiExample(
                    'Nombre demasiado largo',
                    value={'error': 'El nombre no puede superar los 50 caracteres'},
                ),
            ],
        ),
    },
)
@api_view(['GET'])
def demo_saludo(request):
    nombre = request.query_params.get('nombre', 'mundo')
    if len(nombre) > 50:
        return Response(
            {'error': 'El nombre no puede superar los 50 caracteres'},
            status=status.HTTP_400_BAD_REQUEST,
        )
    serializer = DemoSaludoSerializer({
        'mensaje': f'Hola {nombre}',
        'fecha': timezone.now(),
    })
    return Response(serializer.data)


@extend_schema(
    tags=['Demo'],
    summary='Endpoint demo 2: suma de dos números',
    description=(
        'Segundo endpoint de prueba, esta vez un **POST** con cuerpo JSON.\n\n'
        '## Reglas\n'
        '- `a` y `b` son obligatorios y deben ser enteros entre **0 y 1000**.\n'
        '- Devuelve `a + b` en el campo `resultado`.\n\n'
        '> Endpoint solo de prueba: no accede a la base de datos.'
    ),
    request=DemoSumaSerializer,
    examples=[
        OpenApiExample('Suma simple', value={'a': 2, 'b': 3}, request_only=True),
    ],
    responses={
        200: OpenApiResponse(
            response=DemoSumaResultadoSerializer,
            description='Suma calculada correctamente',
            examples=[OpenApiExample('Respuesta exitosa', value={'resultado': 5})],
        ),
        400: OpenApiResponse(
            description='Datos inválidos (faltan campos o están fuera de rango)',
            examples=[
                OpenApiExample('Fuera de rango', value={'a': ['Ensure this value is less than or equal to 1000.']}),
            ],
        ),
    },
)
@api_view(['POST'])
def demo_suma(request):
    serializer = DemoSumaSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    datos = serializer.validated_data
    return Response({'resultado': datos['a'] + datos['b']})
