from functools import wraps
from django.shortcuts import redirect

def clienterole_required():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            usuario = request.user
            if usuario.role == "admin":
                return redirect('usuarios:adminHome')
            elif usuario.role == "vendedor":
                return redirect('usuarios:vendedorHome')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
