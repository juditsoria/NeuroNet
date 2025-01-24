from django.core.exceptions import PermissionDenied

class ClienteRequiredMixin:
    """
    Mixin para restringir el acceso solo a usuarios con perfil de cliente.
    """
    def dispatch(self, request, *args, **kwargs):
        # Permitir acceso solo si el usuario está autenticado y tiene el perfil "cliente"
        if request.user.is_authenticated and request.user.perfil == 'cliente':
            return super().dispatch(request, *args, **kwargs)
        # Lanza un error de permiso denegado si no es un cliente
        raise PermissionDenied("Acceso denegado. Solo los clientes pueden acceder a esta vista.")
    
class NoClientesAllowedMixin:
    """
    Mixin para restringir el acceso a los usuarios con perfil de cliente.
    """
    def dispatch(self, request, *args, **kwargs):
        '''
        - dispatch(request, *args, **kwargs): Comprueba si el usuario está autenticado y si su perfil es "cliente"
        '''
        if request.user.is_authenticated and request.user.perfil == 'cliente':
            raise PermissionDenied("Acceso denegado. Los clientes no pueden acceder a esta vista.")
        # Si no es cliente, permite el acceso
        return super().dispatch(request, *args, **kwargs)
