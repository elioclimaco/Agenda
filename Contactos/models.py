from django.db import models


class Contacto(models.Model):
    Nombres     = models.CharField(max_length = 50)
    Apellidos   = models.CharField(max_length = 50)
    Email       = models.EmailField(max_length = 50)

    def __unicode__(self):
        return ' '.join([self.Nombres, self.Apellidos,])


class Direccion(models.Model):
    contacto        = models.ForeignKey(Contacto)
    TipoDireccion   = models.CharField(max_length = 10)
    Direccion       = models.CharField(max_length = 250)
    Ciudad          = models.CharField(max_length = 250)
    Provincia       = models.CharField(max_length = 50)
    CodigoPostal    = models.CharField(max_length = 50)

    class Meta:
        unique_together = ('contacto', 'TipoDireccion',)