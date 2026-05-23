from django.shortcuts import redirect

def role_required(roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):

            if not request.user.is_authenticated:
                return redirect('login')

            if request.user.rol not in roles:
                return redirect('productos')  # o página error

            return view_func(request, *args, **kwargs)

        return wrapper
    return decorator