from domain.models.profesor import Profesor
from domain.models.asignatura import Asignatura
from application.orchestrator import generar_resumen_general

def test_generar_resumen_general():
    # Crear profesores ficticios
    ana = Profesor("Ana", "López")
    luis = Profesor("Luis", "Martínez")

    # Crear asignaturas (una sin asignar)
    redes = Asignatura("Redes", "M03", "ASIX", "1º", 5)
    bd = Asignatura("Bases de Datos", "M08", "DAW", "2º", 4)
    montaje = Asignatura("Montaje", "M01", "SMX", "1º", 3)

    # Asignar profesores a algunas asignaturas
    redes.asignar_profesor(ana, 5)
    bd.asignar_profesor(luis, 4)

    asignaturas = [redes, bd, montaje]
    profesores = [ana, luis]

    resumen = generar_resumen_general(profesores, asignaturas)

    assert resumen["total_profesores"] == 2
    assert resumen["total_asignaturas"] == 3
    assert resumen["carga_docente"] == 9
    assert len(resumen["sin_asignar"]) == 1
    assert resumen["sin_asignar"][0] == montaje
