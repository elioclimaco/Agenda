# -*- coding: utf-8 -*-
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView
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

    # Vamos a usar la misma plantilla nuevo.html
    # para editar la información de un contacto,
    # para esto vamos a añadir información acerca
    # de donde el formulario debería redireccionar
    # al contexto.
    def get_context_data(self, **kwargs):
        contexto = super(vstaNuevoContacto, self).get_context_data(**kwargs)
        contexto['action'] = reverse('nspContactos:urlNuevo')
        return contexto


class vstaEditarContacto(UpdateView):
    model = Contacto
    template_name = 'contactos/nuevo.html'

    def get_success_url(self):
        return reverse('nspContactos:urlListar')

    def get_context_data(self, **kwargs):
        contexto = super(vstaEditarContacto, self).get_context_data(**kwargs)

        # Del mismo modo que en la vista CrearContacto
        # definimos un contexto, pero en este caso necesitamos
        # el ID del contacto del cual queremos modificar
        # sus datos.
        contacto = {'pk': self.get_object().id}
        contexto['action'] = reverse('nspContactos:urlEditar', kwargs = contacto)
        return contexto


class vstaBorrarContacto(DeleteView):
    model = Contacto
    template_name = 'contactos/eliminar.html'

    def get_success_url(self):
        return reverse('nspContactos:urlListar')


class vstaDetallesContacto(DetailView):
    model = Contacto
    template_name = 'contactos/detalles.html'
