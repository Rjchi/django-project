from django.db import models

# Aqui van los modelos de mi proyecto


# Para poder utilizar los modelos tenemos que conectarlo en el archivo mysite/settings.py

# El parametro que ingresamos es la herencia de los modelos que me da django

class tabla_uno_project(models.Model):
    # Estos atributos me van a servir para especificar las columnas y los
    # datos que voy ha estar guardando en una  tabla

    # Con CharField(aqui va la longitud) es como decir que name va a ser de tipo caracter
    name = models.CharField(max_length=50)

    # Con esto hacemos que nos muestre desde el panel de admin
    # el nombre de los projectos
    def __str__(self):
        return self.name


# Para ejecutar las migraciones es decir los modelos, ejecutar python manage.py makemigrations myapp
# o python manage.py makemigrations
# Con ese comando le decimos que queremos hacer nuevas migraciones en el proyecto a la base de datos
# al ejecutarlo nos va a crear un nuevo archivo 001_innitial... en migrations este archivo contiene
# la tabla del modelo

class modelo_tareas_del_project(models.Model):
    title = models.CharField(max_length=30)
    # TextField() se usa cuando vamos a tener que ingresar una cantidad mayor de caracteres
    description = models.TextField()
    # project ase referencia al proyecto al que pertenece
    # con ForeignKey() decimos que esta tabla tiene una relacion con otra tabla
    # como parametro va el nombre de la tabla con la cual tiene relacion
    # con on_delete= le estaremos diciendo que es lo que tiene que hacer cuando se elimine un proyecto
    #  y con CASCADE le estamos diciendo que cuando se elimine un dato se debe eliminar tambien los datos
    # que tiene relacion con el
    project = models.ForeignKey(tabla_uno_project, on_delete=models.CASCADE)
    # Le decimos que va a tener un valor por defecto en False
    # SIEMPRE SE DEBE MIGRAR CUANDO HACEMOS ESTE TIPO DE CAMBIOS
    done = models.BooleanField(default=False)

    # El self es una referencia a la misma clase
    def __str__(self):
        return f"{self.title} - {self.description} - {self.project.name}"


# Ejecutar python manage.py shell para poder interactuar con un shell especifico de django
# con esto podremos acceder a los modelos que tenemos en la aplicacion myapp (en este caso)

# from myapp.models import tabla_uno_project, modelo_tareas_del_project
# (Para importar las clases (modelos) creados anteriormente)
# ahora creamos un objeto:
# p = tabla_uno_project(name="aplicacion movil")
# y para guardarlo en la base de datos ejecutamos p.save()
# Para listar todos los datos desde python:
# tabla_uno_project.objects.all()    .all() nos trae todos los datos de la tabla
# esto nos da un QuerySet con una lista de objetos
# y para obtener uno en especifico:
# tabla_uno_project.objects.get("name=aplicacion web usando django") <-- (tambien lo puedo buscar por id)
# para cerrar el shell que generamos ejecutamos exit()


# Ahora para ejecutar tareas (modelo_tareas_del_project)
# para guardar una tarea dentro de un proyecto:
# p = tabla_uno_project.objects.get(id=1)
# ahora le decimos desde le proyecto quiero establecer una tarea
# p.modelo_tareas_del_project_set.create(title="descargar ID", description="...", ...)
# ahora para consultar todas las tareas que le pertenecen a un proyecto:
# (p.nombre de la clase_set.all()) p.modelo_tareas_del_project_set.all()
# Consultamos todas las tareas:
# p.modelo_tareas_del_project_set.all()
# el resultado es un querySet para obtener solo una:
# p.modelo_tareas_del_project_set.get(id = 1)

# Ahora si queremos hacer una consulta pero no queremos que nos de error en caso de que no exista
# tabla_uno_project.objects.filter(name__startswith="a" o name="aplicacion ...")
# para ahorrarnos codificacion podemos:
# p = tabla_uno_project.objects y asi p.filter()