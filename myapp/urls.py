# Este archivo se creo con el fin de que cada aplicacion contenga sus propias rutas

from django.urls import path
# Asi importamos todo el archivo:
# Y para hacer uso ya sea de sus funciones se pone views.LoQueQuiero
from myapp import views
# El punto es para referirce a la ruta actual (en este caso es myapp)
from . import views

#  Aqui tenemos las urls que vamos a utilizar
urlpatterns = [
    # En caso de que actualicemos una url, para evitar errores en cualquier parte del proyecto
    # donde llamamos estas url (porque cambia la ruta, lo que nos da un resultado de 404)
    # en django les podemos poner un nombre a estas rutas en caso de una actualizacion la ruta cambia
    # en todos lados
    
    # para poner un nombre a las rutas utilizamos name="index"
    path('', views.index, name="index"),
    # Con esto decimos que entre en la ruta 'ruta/ruta.com/' y que ejecute una funcion que esta dentro de views
    # esta funcion actua como un documento html en este caso (por asi decirlo)
    path('about/', views.about, name="about"),
    # Con esto lo que hacemos es crear una variable que esperamos, y extraerla con la funcion
    # tambien podemos hacerlo con un int ejm: hello/<int:id>
    path('hello/<str:usuario>', views.unaFuncion, name="hello"),

    path('projects/', views.projectos, name="projects"),
    path('task/', views.tareas, name="task"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project")
]