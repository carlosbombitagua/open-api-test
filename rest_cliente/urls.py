from django.urls import path
from .views import lista_clientes, demo_saludo, demo_suma

urlpatterns = [
    path('lista_clientes', lista_clientes, name="lista_clientes"),
    path('demo/saludo', demo_saludo, name="demo_saludo"),
    path('demo/suma', demo_suma, name="demo_suma"),
]