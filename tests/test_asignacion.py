from domain.models.profesor import Profesor
from domain.models.asignatura import Asignatura
from application.orchestrator import asignar_profesor_a_asignatura

def test_asignar_profesor_valido():
    profe = Profesor("Carlos", "Ruiz")
    asignatura = Asignatura("Redes", "M03", "ASIX", "1º", 5)

    asignar_profesor_a_asignatura(profe, asignatura, 3)

    assert asignatura.horas_por_profesor(profe) == 3
    assert profe.asignaturas[0] == asignatura
    assert profe.horas_asignadas == 3
    assert asignatura.esta_asignada()

def test_asignar_profesor_sin_horas():
    profe = Profesor("Sara", "Pérez")
    asignatura = Asignatura("Sistemas", "M05", "DAW", "2º", 4)

    profe.asignaturas.append(asignatura)
    asignatura.distribucion[profe] = Profesor.MAX_HORAS

    try:
        asignar_profesor_a_asignatura(profe, asignatura, 5)
        assert False  # no debe llegar aquí
    except ValueError:
        assert True
