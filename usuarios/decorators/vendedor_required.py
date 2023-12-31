from functools import wraps
from django.shortcuts import redirect

def vendedorrole_required():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            usuario = request.user
            if usuario.role == "cliente":
                return redirect('productos:index')
            elif usuario.role == "admin":
                return redirect('usuarios:adminHome')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
