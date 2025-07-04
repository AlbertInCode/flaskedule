import json
from config import PROFESORES_FILE, ASIGNATURAS_FILE

def guardar_profesores(profesores, path=PROFESORES_FILE):
    export = [{"nombre": p.nombre, "apellido": p.apellido, "tutor_de": p.tutor_de} for p in profesores]
    with open(path, 'w') as f:
        json.dump(export, f, indent=2)

def guardar_asignaturas(asignaturas, path=ASIGNATURAS_FILE):
    export = []
    for a in asignaturas:
        nombres = [p.nombre for p in a.profesores()]
        export.append({
            "nombre": a.nombre,
            "modulo": a.modulo,
            "ciclo": a.ciclo,
            "curso": a.curso,
            "horas": a.horas,
            "profesores": nombres
        })
    with open(path, 'w') as f:
        json.dump(export, f, indent=2)
