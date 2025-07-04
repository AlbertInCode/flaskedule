import json
from domain.models.profesor import Profesor
from domain.models.asignatura import Asignatura
from config import PROFESORES_FILE, ASIGNATURAS_FILE

def cargar_profesores(path=PROFESORES_FILE):
    with open(path) as f:
        data = json.load(f)
    return [Profesor(p['nombre'], p['apellido']) for p in data]

def cargar_asignaturas(path=ASIGNATURAS_FILE, profesores=[]):
    with open(path) as f:
        data = json.load(f)
    resultado = []
    for a in data:
        asignatura = Asignatura(a['nombre'], a['modulo'], a['ciclo'], a['curso'], a['horas'])
        for nombre in a.get('profesores', []):
            profe = next((p for p in profesores if p.nombre == nombre), None)
            if profe:
                asignatura.asignar_profesor(profe, a['horas'])
        resultado.append(asignatura)
    return resultado
