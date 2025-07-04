import os

# Rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATES_DIR = os.path.join(BASE_DIR, 'interfaces', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
DATA_DIR = os.path.join(BASE_DIR, 'data')

PROFESORES_FILE = os.path.join(DATA_DIR, 'profesores.json')
ASIGNATURAS_FILE = os.path.join(DATA_DIR, 'asignaturas.json')

# Configuración general
MAX_HORAS_PROFESOR = 18
