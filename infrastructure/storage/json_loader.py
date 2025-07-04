import json
from domain.models.profesor import Profesor
from domain.models.asignatura import Asignatura

def cargar_profesores(ruta='data/profesores.json'):
    with open(ruta, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return [Profesor(p['nombre'], p['apellido']) for p in data]

def cargar_asignaturas(ruta='data/asignaturas.json', profesores=[]):
    with open(ruta, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    asignaturas = []
    for a in data:
        asignatura = Asignatura(a['nombre'], a['modulo'], a['ciclo'], a['curso'], a['horas'])
        for nombre in a.get('profesores', []):
            profesor = next((p for p in profesores if p.nombre == nombre), None)
            if profesor:
                asignatura.asignar_profesor(profesor, a['horas'])
        asignaturas.append(asignatura)
    
    return asignaturas

