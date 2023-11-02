from django.contrib import admin
# Importamos nuestros modelos
from .models import modelo_tareas_del_project, tabla_uno_project

# python manage.py createsuperuser (para crear un admin)
# ruta /admin
# Este archivo es para que en nuestra aplicacion se pueda añadir determinados modelos (mis models.py)
# al panel de administrador

# Aqui le decimos desde admin llamame ...
# con esto se crea una seccion nueva en el panel de administrador
admin.site.register(tabla_uno_project)
admin.site.register(modelo_tareas_del_project)