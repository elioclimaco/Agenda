# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from .views import *

urlpatterns = patterns('',
    url(r'^$', vstaListarContactos.as_view(), name = 'urlListar'),
    url(r'^nuevo/$', vstaNuevoContacto.as_view(), name = 'urlNuevo'),
)
