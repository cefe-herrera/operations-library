# Dockerfile

# Usar la imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos del proyecto al contenedor
COPY . .

# Instalar la biblioteca localmente
RUN pip install .

# Comando por defecto para ejecutar las pruebas
CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
