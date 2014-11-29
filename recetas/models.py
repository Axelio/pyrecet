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
    porcion = models.IntegerPositiveField()
    cantidad = models.DecimalFields(digits=100, max_decimals=3)
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
    paso = models.IntegerPositiveField()
    detalle = models.TextField()

    class Meta:
        db_table = 'preparacion'
        verbose_name_plural = 'preparaciones'

    def __unicode__(self):
        return '%s. %s' % (self.paso, self.detalle)


class Rendimiento(models.Model):
    receta = models.ForeignKey('Receta')
    porcion = models.IntegerPositiveField()
    cantidad = models.DecimalFields(digits=100, max_decimals=3)
    unidades = models.BooleanField(default=False)
    observaciones = models.BooleanField(default=False)

    class Meta:
        db_table = 'rendimiento'

    def __unicode__(self):
        return '%s. %s' % (self.receta, self.porcion)
