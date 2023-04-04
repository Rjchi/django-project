# Importamos JsonRespon para poder devolver un formato que el navegador pueda
# entender
from django.http import HttpResponse, JsonResponse
# fn + f1 settings (JSON) ---> "editor.wordWarp": "on"
# Importamos render para renderizar paginas y redirect para redireccionar al usuario a otra ruta
from django.shortcuts import render, redirect

# Importamos los modelos para hacer consultas a la base de datos
from .models import tabla_uno_project, modelo_tareas_del_project

# Importamos el formulario que hemos creado por medio de codigo python
from .forms import create_new_task, create_new_project

# Devolvemos una pagina 404 en caso de un error a traves de una funcion
# propia de django
from django.shortcuts import get_object_or_404

# LA CONVENCION RECOMENDADA PARA PYTHON ES Snake Case variable_uno
# El patron de diseño que generalmente se utiliza en django es el MTV
# Modelo, Plantilla, Vista
# La logica de negocio va en la vista(la vista en este caso es similar
# al controlador del patron MVC) y las vistas serian las plantillas

# 1- Instalar python
# 2- Crear una carpeta
# 3- Ponerse en la carpeta (desde CMD) y ejecutar pip install virtualenv
# El virtualenv (entorno virtual) es para no tener problemas con las dependencias en
# caso de que tengamos mas de un proyecto con python
# 4- Ejecutar virtualenv venv para crear la carpeta que contiene las configuraciones
# Para trabajar en el entorno virtual
# 5- Ejecutar .\venv\Scripts\activate para activar el entorno virtual
# 6- Ejecutar code .
# 7- Si se tiene problemas con la activacion instalar la extension powerShell
# 7.1 - La primera vez debes que cambiar la politica de seguridad en Windows para que te permita ejecutarlos.
# 7.2 - Ejecutar: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# 8- Ejecutar en el powerShell .\venv\Scripts\activate.ps1 (verificar la extension del archivo)
# 9- Ejecutar pip install django
# 10- Podemos ver la version con el siguiente comando django-admin --version
# 11- Ejecutar django-admin startproject NOMBRE . para crear el proyecto
# 12- Ejecutar python manage.py runserver 3000(Aqui va el puerto (en caso de coincidencias con otros proyectos))
# Ctrl + click en la url de la terminal
# 13- Los proyectos de django se dividen en carpetas denominadas Apps para crearlas ejecutar
# python manage.py startapp Nombre (no usar django (palabras reservadas) para evitar errores)
# Ctrl + C (Break)
# 14- En caso de trabajar con la DB mysql ejecutar despues de configurar la conexion pip install pymysql
# 15- Y importar en el init.py del nucleo del proyecto import pymysql y tambien pymysql.install_as_MySQLdb()
# 16- y tambien en senttings.py import pymysql y pymysql.install_as_MySQLdb()

# Nota: Django nos genera una base de datos que podemos utilizar en el desarrollo
# en producción debemos cambiarla por otro motor

# Para desactivar el entorno virtual ejecutar Scripts\deactivate.bat

# Para visualizar la base de datos que se nos genero por defecto en el proyecto
# se debe instalar db browser for sqlite (ese programa nos permite poder ver la interfaz grafica
# de la base de datos)
# DB Browser for SQLite - PortableApp este
# Agregamos el archivo .sqlite3 (en Browse Data)
# Y ejecutamos en la terminal python manage.py makemigrations | python manage.py migrate
# y f5 en la aplicacion (se visualizara la base de datos que trae por defecto django
# con su  ORM (las tablas ya traen funciones para insertar datos))
# Debemos crear un modelo para poder gestionar la base de datos (me refiero a insertar datos, actulizarlos
# crear tablas...) El modelo se va a transformar en una tabla de SQL (esto va en el archivo models.py)

# Estas funciones se desarrollaron con la intencion de hacer pruebas
# por lo general estas las utilizamos para enviar interfaces al usuario
# utilizando Tamplates (PLANTILLAS) archivos HTML que se encuentran en
# la carpeta templetes (que creamos) la cual contiene archivos HTML
# Asi (primero importamos render):


def index(request):
    # Dato de ejemplo:
    # para mostrar este dato en el archivo html se lo pasamos como un tercer
    title = 'Django Cours'
    # parametro a render en este caso.
    # y ahora index tiene la variable title
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = 'Richi'
    return render(request, 'about.html', {
        'username': username
    })


def unaFuncion(request, usuario):
    # Con HttpResponse Retornamos los datos de un modelo.
    # con %s() %(reemplace) podemos concatenear una variable en el dom
    return HttpResponse("<h2>Hello %s</h2>" % usuario)


def projectos(request):
    # Obtenemos el QuerySet y lo convetimos en una lista
    # con values() obtenemos solamente los valores
   # projects = list(tabla_uno_project.objects.values())
    projects = tabla_uno_project.objects.all()
    # Utilizamos el JsonResponse
    # return JsonResponse(projects, safe=False)
    return render(request, 'projects.html', {
        'projects': projects
    })


# Consulta a la base de datos apartir de un parametro
# def tareas(request, id):
def tareas(request):
    tasks = modelo_tareas_del_project.objects.all()
    # task = modelo_tareas_del_project.objects.get(id=id)
    # Esto es lo mismo de arriba pero con mas control en las busquedas sin resultado
    # task = get_object_or_404(modelo_tareas_del_project, id = id)
    # return HttpResponse('task: %s' % task.title)
    return render(request, 'task.html', {
        'tasks': tasks
    })


def create_task(request):
    # Ahora vamos ha hacer una validacion (si me estan visitando a traves del metodo GET mostrar interfaz)
    if request.method == 'GET':
        # Mostrar interfaz
        # En el tercer paremetro le vamos a pasar el formulario recien creado en forms.py
        return render(request, 'create_task.html', {
        # Con esto generamos el nuevo formulario
            'forms': create_new_task()
        })
    # Y este es por si me visitan desde el metodo post (para guardar los datos del formulario)
    else:
        # Para insertar los valores en la base de datos podemos hacer uso del metodo GET
        # que lo que hace es tomar la consulta que hace el usuario de la url
        # por medio del name= que le dimos a los inputs
        # modelo_tareas_del_project.objects.create(title=request.GET['title'],
        #                                          description=request.GET['description'],
        #                                          project_id=2)

        modelo_tareas_del_project.objects.create(title=request.POST['title'],
                                                  description=request.POST['description'],
                                                  project_id=2)
        # Y aqui redireccionamos al usuario a la pagina que lista las tareas
        # Y aqui lo que decimos es desde la ruta inicial "/" mandame a "task/"
      # return redirect('/task/')

        # Aqui estamos haciendo uso de los nombres que le dimos a las rutas en myapp/urls.py 
        return redirect('task')

# Funcion para crear proyectos desde un formulario
def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'forms' : create_new_project()
        })
    else:
        tabla_uno_project.objects.create(name=request.POST['name'])
        # return redirect('/projects/')
        # haciendo uso del name= para las urls
        return redirect('projects')
