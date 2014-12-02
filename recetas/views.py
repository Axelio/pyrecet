from django.shortcuts import render
from django.views.generic.base import View
from django.core.context_processors import csrf

from .models import Receta
from .forms import RecetaForm


class RecetaView(View):

    diccionario = {}
    template_name = 'index.html'
    form = RecetaForm

    def get(self, request, *args, **kwargs):
        self.diccionario.update(csrf(request))
        self.diccionario.update({'form': self.form()})
        return render(request, template_name=self.template_name,
                      dictionary=self.diccionario)

    def post(self, request, *args, **kwargs):
        self.form = self.form(request.POST)
        receta_list = Receta.objects.all()
        nombre = request.POST['nombre']
        ingrediente = request.POST['ingrediente']
        if self.form.is_valid():
            if request.POST.has_key('nombre'):
                receta_list = receta_list.filter(nombre__icontains=nombre)
            if request.POST.has_key('ingrediente'):
                receta_list = receta_list.filter(
                    ingrediente__ingrediente_id__nombre__icontains=ingrediente)
            self.template_name = 'receta_list.html'
        self.diccionario.update({'receta_list': receta_list})
        self.diccionario.update(csrf(request))
        self.diccionario.update({'form': self.form})
        return render(request,
                      template_name=self.template_name,
                      dictionary=self.diccionario,
                      )
