from django.contrib import admin
from .models import Categoria, Comida, Usuario, Cliente

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Comida)
admin.site.register(Usuario)
admin.site.register(Cliente)