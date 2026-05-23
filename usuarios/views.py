from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Usuario
from usuarios.decorators import role_required


def registro(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        rol = request.POST.get("rol")

        user = Usuario.objects.create_user(
            username=username,
            password=password,
            rol=rol
        )

        @role_required(['cliente', 'vendedor', 'admin'])
        def productos(request):
            return render(request, "productos/tienda.html")
        
        @role_required(['vendedor', 'admin'])
        def crear_producto(request):
            return render(request, "productos/crear.html")
        
        @role_required(['admin'])
        def panel_admin(request):
            return render(request, "admin/panel.html")

        # login automático después del registro (opcional)
        login(request, user)

        return redirect('productos')
    return render(request, "usuarios/registro.html")


def login_view(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('productos')
        else:
            error = "Credenciales incorrectas"

    return render(request, "usuarios/login.html", {"error": error})


def logout_view(request):
    logout(request)
    return redirect('login')