from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# establece la variable de entorno DJANGO_SETTINGS_MODULE para el archivo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_learning.settings')

app = Celery('e_learning')

# Utiliza la configuración de Django para la configuración de Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Aquí es donde agregas la configuración broker_connection_retry_on_startup
app.conf.broker_connection_retry_on_startup = True

# Carga automáticamente las tareas definidas en tus aplicaciones de Django
app.autodiscover_tasks()
