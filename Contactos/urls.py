# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from .views import *

urlpatterns = patterns('',
    url(r'^$', vstaListarContactos.as_view(), name = 'urlListar'),
    url(r'^nuevo/$', vstaNuevoContacto.as_view(), name = 'urlNuevo'),
    url(r'^editar/(?P<pk>\d+)/$', vstaEditarContacto.as_view(), name = 'urlEditar'),
    url(r'^borrar/(?P<pk>\d+)/$', vstaBorrarContacto.as_view(), name = 'urlBorrar'),
    url(r'^detalles/(?P<pk>\d+)/$', vstaDetallesContacto.as_view(), name = 'urlDetalles'),
)
