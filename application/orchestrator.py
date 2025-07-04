from domain.models.profesor import Profesor
from domain.models.asignatura import Asignatura

def asignar_profesor_a_asignatura(profesor: Profesor, asignatura: Asignatura, horas: int):
    if profesor.horas_disponibles() < horas:
        raise ValueError(f"El profesor {profesor.nombre} no tiene suficientes horas disponibles.")
    
    if sum(asignatura.distribucion.values()) + horas > asignatura.horas:
        raise ValueError(f"La asignatura {asignatura.nombre} ya está cubierta o excedida.")

    asignatura.asignar_profesor(profesor, horas)

def quitar_profesor_de_asignatura(profesor: Profesor, asignatura: Asignatura):
    if profesor in asignatura.distribucion:
        del asignatura.distribucion[profesor]
        if asignatura in profesor.asignaturas:
            profesor.asignaturas.remove(asignatura)

def generar_resumen_general(profesores: list, asignaturas: list) -> dict:
    sin_asignar = [a for a in asignaturas if not a.esta_asignada()]
    total_horas = sum(p.horas_asignadas for p in profesores)
    return {
        "total_profesores": len(profesores),
        "total_asignaturas": len(asignaturas),
        "sin_asignar": sin_asignar,
        "carga_docente": total_horas
    }
