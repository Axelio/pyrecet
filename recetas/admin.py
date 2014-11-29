from django.contrib import admin
from .models import *


class IngredienteInline(admin.TabularInline):
    model = Ingrediente
    extra = 1


class PreparacionInline(admin.TabularInline):
    model = Preparacion
    extra = 1


class RendimientoInline(admin.TabularInline):
    model = Rendimiento
    extra = 1


@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    search_field = ('nombre',)
    list_display = ('nombre', 'tipo')
    list_filter = ('tipo',)
    inlines = (IngredienteInline, PreparacionInline, RendimientoInline)


@admin.register(TipoReceta)
class TipoRecetaAdmin(admin.ModelAdmin):
    search_field = ('nombre',)
    ordering = ('nombre',)


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    search_field = ('receta', 'ingrediente', 'porcion')
    list_display = ('receta', 'ingrediente', 'porcion', 'cantidad', 'unidades')


@admin.register(IngredienteDetalle)
class IngredienteDetalleAdmin(admin.ModelAdmin):
    search_field = ('nombre',)
    ordering = ('nombre',)


@admin.register(Preparacion)
class PreparacionAdmin(admin.ModelAdmin):
    list_display = ('paso', 'receta')
    search_field = ('paso',)
    ordering = ('paso',)


@admin.register(Rendimiento)
class RendimientoAdmin(admin.ModelAdmin):
    list_display = ('receta', 'porcion', 'cantidad', 'unidades')
    search_field = ('receta',)
    ordering = ('receta',)
