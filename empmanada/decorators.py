from django.conf import settings
from django.core.exceptions import PermissionDenied
from functools import wraps


def docs_access_required(view):
    """Solo permite el paso a miembros del grupo DOCS_GROUP_NAME (y superusuarios).

    Anónimos y usuarios sin acceso reciben 403, que se muestra con la plantilla
    403.html (mensaje "no tienes acceso" y, si no hay sesión, botón de login).
    """
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        user = request.user
        tiene_acceso = user.is_authenticated and (
            user.is_superuser or user.groups.filter(name=settings.DOCS_GROUP_NAME).exists()
        )
        if not tiene_acceso:
            raise PermissionDenied
        return view(request, *args, **kwargs)
    return wrapper
