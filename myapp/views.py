from django.http import HttpResponse
# Create your views here.
# LA CONVENCION RECOMENDADA PARA PYTHON ES Snake Case variable_uno

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
# 8- Ejecutar en el powerShell .\venv\Scripts\activate.ps1 (verificar la extension del archivo)
# 9- Ejecutar pip install django
# 10- Podemos ver la version con el siguiente comando django-admin --version
# 11- Ejecutar django-admin startproject NOMBRE . para crear el proyecto
# 12- Ejecutar python manage.py runserver 3000(Aqui va el puerto (en caso de coincidencias con otros proyectos))
# Ctrl + click en la url de la terminal
# 13- Los proyectos de django se dividen en carpetas denominadas Apps para crearlas ejecutar
# python manage.py startapp Nombre (no usar django (palabras reservadas) para evitar errores)
# Ctrl + C (Break)

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
# 


def unaFuncion(request):
    # Con HttpResponse Retornamos los datos de un modelo.
    return HttpResponse("<h2>Hello World</h2>")


def about(request):
    return HttpResponse('About')
