from django.urls import path 
from .views import index, quienSomos, contacto, galeria, registrarse, from_modcomida, form_comida, mostrar, form_del_comida, form_cliente, form_modcliente, form_del_cliente, clientes

urlpatterns = [
    path('', index, name="index"),
    path('quienSomos/', quienSomos, name="quienSomos"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('registrarse/', registrarse, name="registrarse"),
    path('mostrar/', mostrar, name="mostrar"),
    path('form_comida/', form_comida, name="form_comida"),
    path('from_modcomida/<id>', from_modcomida, name="from_modcomida"),
    path('form_del_comida/<id>', form_del_comida, name="form_del_comida"),
    path('form_cliente', form_cliente, name="form_cliente"),
    path('form_modcliente/<id>', form_modcliente, name="form_modcliente"),
    path('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente"),
    path('clientes/', clientes, name="clientes"),

]
