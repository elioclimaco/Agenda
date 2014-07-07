# -*- coding: utf-8 -*-
from django.views.generic import View, ListView, CreateView
from django.core.urlresolvers import reverse

from .models import Contacto

# Código básico de una vista basada en clases
# from django.http import HttpResponse
# class MiVista(View):
#    def get(self, peticion, *args, **kwargs):
#        return HttpResponse("Hola Mundo")


class vstaListarContactos(ListView):
    model = Contacto
    template_name = 'contactos/listar.html'


class vstaNuevoContacto(CreateView):
    model = Contacto
    template_name = 'contactos/nuevo.html'

    # Sobre escribimos el método success_url para
    # redireccionar al usuario cuando el formulario
    # se procese o envíe de manera satisfactoria.
    # Tambien se puede usar el metodo success_url
    # de la siguiente forma:
    # success_url = reverse_lazy('urlListar').
    def get_success_url(self):
        return reverse('nspContactos:urlListar')