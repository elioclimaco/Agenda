from django.db import models
from django.core.urlresolvers import reverse


class Contacto(models.Model):
    Nombres     = models.CharField(max_length = 50)
    Apellidos   = models.CharField(max_length = 50)
    Email       = models.EmailField(max_length = 50)

    def __unicode__(self):
        return ' '.join([self.Nombres, self.Apellidos,])

    def get_absolute_url(self):
        return reverse('nspContactos:urlDetalles', kwargs = {'pk': self.id})

class Direccion(models.Model):
    contacto        = models.ForeignKey(Contacto)
    TipoDireccion   = models.CharField(max_length = 10)
    Direccion       = models.CharField(max_length = 250)
    Ciudad          = models.CharField(max_length = 250)
    Provincia       = models.CharField(max_length = 50)
    CodigoPostal    = models.CharField(max_length = 50)

    class Meta:
        unique_together = ('contacto', 'TipoDireccion',)

    def __unicode__(self):
        return ' '.join([self.TipoDireccion, self.Direccion,])