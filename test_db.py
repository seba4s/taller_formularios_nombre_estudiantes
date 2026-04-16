import os
import django
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv('.env')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taller_formularios_nombre_estudiantes.settings')
django.setup()

from django.db import connection
from django.conf import settings

try:
    # Obtener el engine de la BD
    db_engine = settings.DATABASES['default']['ENGINE']
    db_name = settings.DATABASES['default']['NAME']
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
    
    print("✅ Conexión a la BD exitosa")
    print(f"Engine: {db_engine}")
    print(f"Base de datos: {db_name}")
except Exception as e:
    print(f"❌ Error de conexión: {e}")
