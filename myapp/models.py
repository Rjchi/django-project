from django.db import models

# Aqui van los modelos de mi proyecto


# Para poder utilizar los modelos debemos que conectarlo en el archivo mysite/settings.py

# El parametro que ingresamos es la herencia de los modelos que me da django

class tabla_uno_project(models.Model):
    # Estos atributos me van a servir para especificar las columnas y los
    # datos que voy ha estar guardando en una  tabla

    # Con CharField(aqui va la longitud) es como decir que name va a ser de tipo caracter
    name = models.CharField(max_length=50)
