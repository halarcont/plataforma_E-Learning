# Usar una imagen base de Python
FROM python:3.8

# Establecer variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crear y establecer el directorio de trabajo
RUN mkdir /codigo
WORKDIR /codigo

# Instalar dependencias
COPY requirements.txt /codigo/
RUN pip install -r requirements.txt

# Copiar el proyecto
COPY . /codigo/
