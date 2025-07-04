import json
from models import Profesor, Asignatura

def cargar_profesores(filename='data/profesores.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    profesores = []
    for p in data:
        profe = Profesor(p["nombre"], p["apellido"])
        profe.horas_asignadas = p.get("horas_asignadas", 0)
        profesores.append(profe)
    return profesores

def guardar_profesores(profesores, filename='data/profesores.json'):
    data = []
    for p in profesores:
        data.append({
            "nombre": p.nombre,
            "apellido": p.apellido,
            "horas_asignadas": p.horas_asignadas
        })
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def cargar_asignaturas(filename='data/asignaturas.json', profesores=None):
    with open(filename, 'r') as f:
        data = json.load(f)
    asignaturas = []
    for a in data:
        asig = Asignatura(a["nombre"], a["modulo"], a["ciclo"], a["curso"], a["horas"])
        if profesores:
            for nombre in a.get("profesores", []):
                profe = next((p for p in profesores if p.nombre == nombre), None)
                if profe:
                    asig.profesores.append(profe)
                    profe.asignaturas.append(asig)
                    profe.horas_asignadas += a["horas"]  # o parte proporcional si hay codocencia
        asignaturas.append(asig)
    return asignaturas


def guardar_asignaturas(asignaturas, filename='data/asignaturas.json'):
    data = []
    for a in asignaturas:
        data.append({
            "nombre": a.nombre,
            "modulo": a.modulo,
            "curso": a.curso,
            "horas": a.horas,
            "profesores": [p.nombre if hasattr(p, "nombre") else p for p in a.profesores]
        })
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
