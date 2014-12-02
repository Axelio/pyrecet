# -*- coding: UTF8 -*-
from django.db import models


class Receta(models.Model):
    nombre = models.CharField(max_length=256)
    tipo = models.ForeignKey('TipoReceta')
    imagen = models.ImageField(upload_to='recetas', blank=True)

    class Meta:
        db_table = 'receta'

    def __unicode__(self):
        return '%s' % (self.nombre)


class TipoReceta(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'tipo_receta'

    def __unicode__(self):
        return '%s' % (self.nombre)


class Ingrediente(models.Model):
    receta = models.ForeignKey('Receta')
    ingrediente = models.ForeignKey('IngredienteDetalle')
    porcion = models.PositiveIntegerField(verbose_name=u'porción')
    cantidad = models.DecimalField(max_digits=100,
                                   decimal_places=3,
                                   help_text='En gramos.')
    unidades = models.BooleanField(default=False)

    class Meta:
        db_table = 'ingrediente'

    def __unicode__(self):
        return '%s. %s' % (self.receta, self.ingrediente)


class IngredienteDetalle(models.Model):
    nombre = models.CharField(max_length=256)

    class Meta:
        db_table = 'ingrediente_detalle'

    def __unicode__(self):
        return '%s' % (self.nombre)


class Preparacion(models.Model):
    paso = models.PositiveIntegerField()
    detalle = models.TextField()
    receta = models.ForeignKey('Receta')

    class Meta:
        db_table = 'preparacion'
        verbose_name_plural = 'preparaciones'

    def __unicode__(self):
        return '%s. %s' % (self.paso, self.detalle)


class Rendimiento(models.Model):
    receta = models.ForeignKey('Receta')
    porcion = models.PositiveIntegerField(verbose_name=u'porción')
    cantidad = models.DecimalField(max_digits=100,
                                   decimal_places=3,
                                   help_text='En gramos.')
    unidades = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True)

    class Meta:
        db_table = 'rendimiento'

    def __unicode__(self):
        return '%s. %s' % (self.receta, self.porcion)
