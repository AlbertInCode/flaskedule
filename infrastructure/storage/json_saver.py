import json

def guardar_profesores(profesores, ruta='data/profesores.json'):
    export = [{"nombre": p.nombre, "apellido": p.apellido, "tutor_de": p.tutor_de} for p in profesores]
    with open(ruta, 'w', encoding='utf-8') as file:
        json.dump(export, file, ensure_ascii=False, indent=2)

def guardar_asignaturas(asignaturas, ruta='data/asignaturas.json'):
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
    with open(ruta, 'w', encoding='utf-8') as file:
        json.dump(export, file, ensure_ascii=False, indent=2)