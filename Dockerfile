# Usa una imagen base de Python. Elige la versión de Python que necesitas.
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor.
WORKDIR /app

# Copia los archivos de requisitos a la imagen.
COPY requirements.txt .

# Instala las dependencias desde requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de la aplicación al directorio de trabajo.
COPY . .

# Expone el puerto en el que tu aplicación escuchará (opcional si se usa un servidor web específico).
# EXPOSE 5000

# Especifica el comando para ejecutar tu aplicación.
CMD ["python", "app.py"]
