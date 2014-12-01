# -*- coding: utf-8 -*-
from django import forms
from .models import *


class RecetaForm(forms.Form):
    nombre = forms.CharField(
        max_length=256,
        required=False,
        help_text=u'Ingrese el nombre o parte del nombre de la receta que busca.')
    ingrediente = forms.CharField(
        max_length=256,
        required=False,
        help_text=u'Ingrese algún incrediente de la receta que busca.')

    def clean(self):
        if self.cleaned_data['nombre'] == '' and self.cleaned_data['ingrediente'] == '':
            forms.ValidationError('Debe ingresar un nombre o un ingrediente.')
