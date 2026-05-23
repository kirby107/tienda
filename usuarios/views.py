from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth import login

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_productos')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})