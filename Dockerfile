FROM python:3.9-slim

WORKDIR /app

# Copiamos los requisitos primero si tienes un requirements.txt
# Si no, instalamos flask directamente
RUN pip install flask

# Copiamos todo el contenido de la carpeta actual al directorio /app del contenedor
COPY . /app

# Verificamos que el archivo esté ahí durante la construcción (verás esto en la terminal)
RUN ls -la /app

EXPOSE 5000

# Usamos la ruta absoluta para evitar errores de directorio
CMD ["python", "/app/app.py"]