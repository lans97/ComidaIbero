# ¿Por qué Django?

A partir de ahora tenemos aproximadamente 2 meses (probablemente menos) para realizar un MVP  (Minimum Viable Product)
y necesitamos generar valor tan pronto sea posible. A parte si vamos a recibir ayuda un lenguaje como Python nos
da mucha mayor flexibilidad en desarrollo gracias a su simplicidad.

Django parece ser un framework bastante amable y la herramienta que más nos va a catapultar hacia un buen producto
con los recursos que tenemos acutalmente.

Justo ahora estamos deshaciendonos de los archivos viejos y generando un proyecto vacío de Django.

## Instrucciones

Para correr el sitio es MUY recomendable hacer un entorno virual de Python, instalar las dependencias a este entorno
virtual y activar el servicio con Django:

~~~
python -m venv .venv # Crea un entorno virtual en el folder ".venv"
# Activa el entorno virtual
./.venv/Scripts/Activate.ps1 # Windows Powershell
# ./.venv/Scripts/activate.bat # Windows cmd
# source .venv/scripts/activate # Unix Systems
python -m pip install -r requirements.txt # Instala las dependencias del proyecto en el entorno virtual
python manage.py runserver # Abre el sitio en http//localhost:8000
~~~