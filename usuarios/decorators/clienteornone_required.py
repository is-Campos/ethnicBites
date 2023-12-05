from functools import wraps
from django.shortcuts import redirect

def clienteornone_required():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                usuario = request.user
                if hasattr(usuario, 'role') and usuario.role == "vendedor":
                    return redirect('usuarios:vendedorHome')
                elif hasattr(usuario, 'role') and usuario.role == "admin":
                    return redirect('usuarios:adminHome')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
