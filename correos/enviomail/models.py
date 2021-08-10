from django.db import models

# Create your models here.

class RegistroEnvioMail(models.Model):
    numero_factura = models.CharField('Numero de Factura',max_length=15)
    fecha_envio = models.DateTimeField('Fecha de Envio')
    Estado = models.CharField('Estado', max_length=10)
    archivo = models.CharField('Archivo', max_length=100)
    ruta = models.CharField('Ruta', max_length=300, null=True)