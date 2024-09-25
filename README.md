# ComidaIbero
Proyecto Final de Arquitectura de Software Otoño 2023
Nombre sujeto a cambios.

## Instrucciones

Para correr el sitio es MUY recomendable hacer un entorno virual de Python, instalar las dependencias a este entorno
virtual y activar el servicio con Django:

~~~
python -m venv .venv # Crea un entorno virtual en el folder ".venv"
# Activa el entorno virtual
# ./.venv/Scripts/Activate.ps1 # Windows Powershell
# ./.venv/Scripts/activate.bat # Windows cmd
# source .venv/bin/activate # Unix
python -m pip install -r requirements.txt # Instala las dependencias del proyecto en el entorno virtual
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser # Llena información para crear un administrador
python manage.py runserver # Abre el sitio en http//localhost:8000
~~~

Una vez activo el servidor, visita el link en consola o entra en http://localhost:8000/admin, ingresa sesión con el superusuario creado y llena los modelos necesarios.

Este proyecto no carga automáticamente los recursos en el drive (posible mejora)

## Recursos
En [esta carpeta](https://drive.google.com/drive/folders/1ZTkvD1_7hGe89xfl13xd2L3vC9TF4rSe?usp=drive_linkhttps://drive.google.com/drive/folders/1ZTkvD1_7hGe89xfl13xd2L3vC9TF4rSe?usp=drive_link) se encuentran los recursos generados en Figma. Sólo se incluyeron las pantallas de dos restaurantes como referencia.

