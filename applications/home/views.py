
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django import template
from applications.usuarios_inova.views import *

# Create your views here.

@login_required
def indexPage(request):
    user=request.user
    print(user)
    return render(request,'home/inicio.html')


@login_required
def indexPage(request):
    user=request.user
    rol=request.user.rol
    print(user,rol)
    usuario_log.objects.update(usuario=str(user))
    usuario_log.objects.update(rol=rol)
    return render(request,'home/inicio.html')