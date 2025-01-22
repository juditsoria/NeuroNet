from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    

class Reserva(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    fecha_reserva = models.DateTimeField()
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=15)
    servicio = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Reserva de {self.nombre_cliente} para {self.servicio} el {self.fecha_reserva}"
    
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Recurso(models.Model):
    tipo = models.CharField(max_length=50, choices=[('artículo', 'Artículo'), ('video', 'Video'), ('podcast', 'Podcast')])
    titulo = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, related_name='recursos', on_delete=models.CASCADE)
    contenido = models.TextField()
    enlace = models.URLField()



