from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.

def Index(request):
    return render(request, 'index.html')

def ingreso(request):
    datos = {
        'form': UsuarioForm()
    }

    if request.method == 'POST': 
        usuario = UsuarioForm(request.POST, files=request.FILES)
        if usuario.is_valid():
            usuario.save()         
            return redirect('lista')
    else: 
        usuario = UsuarioForm()

    return render(request, 'core/contactenos.html', {'usuario': usuario})

def lista(request):
    usuario=Usuario.objects.all()
    return render(request, 'core/feedback.html', context={'usuarios':usuario})

def mod_partners(request, id):
    usuario= Usuario.objects.get(RutUsuario=id)

    datos ={
        'form': UsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance = usuario, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            return redirect('lista')
    return render(request, 'core/mod_feedback.html', datos)

def del_partners(request,id):
    usuario = Usuario.objects.get(RutUsuario=id)
    usuario.delete()
    return redirect('lista')