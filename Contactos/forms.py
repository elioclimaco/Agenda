# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory

from .models import Contacto, Direccion

# Agregando un campo de confirmación de
# correo electrónico.
class frmNuevoContacto(forms.ModelForm):
    Nombres         = forms.CharField\
    (
        label       = 'Nombres:',
        required    = True,
        widget      = forms.TextInput
        (
            attrs   = {'placeholder': 'Nombres del contacto'}
        )
    )

    Apellidos       = forms.CharField\
    (
        label       = 'Apellidos:',
        required    = True,
        widget      = forms.TextInput
        (
            attrs   = {'placeholder': 'Apellidos del contacto'}
        )
    )

    Email   = forms.EmailField\
    (
        label       ="Correo electrónico:",
        required    = True,
        widget      =forms.TextInput
            (
                attrs={'placeholder': 'ejem. usuario@ejemplo.com'}
            )
    )

    ConfirmaEmail   = forms.EmailField\
    (
        label       ="Confirmar Correo",
        required    = True,
        widget      =forms.TextInput
            (
                attrs={'placeholder': 'Confirmación de correo electrónico'}
            )
    )

    # Asociamos el formulario frmNuevoContacto
    # al modelo Contacto.
    class Meta:
        model = Contacto

    def __init__self(self, *args, **kwargs):
        if kwargs.get('instance'):
            email = kwargs['instance'].Email
            kwargs.setdefault('initial', {})['ConfirmaEmail'] = email

        return super(frmNuevoContacto, self).__init__(*args, **kwargs)

    # Personalizando la validación del campo
    # ConfirmaEmail.
    def clean(self):
        if (self.cleaned_data.get('Email') != self.cleaned_data.get('ConfirmaEmail')):
            raise ValidationError('Los correos electrónicos no coinciden')

        return self.cleaned_data


frmSetDireccionContacto = inlineformset_factory(
    Contacto,
    Direccion,
)

