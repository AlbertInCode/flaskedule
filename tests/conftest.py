import pytest
from domain.models.profesor import Profesor
from domain.models.asignatura import Asignatura

@pytest.fixture
def profesores():
    ana = Profesor("Ana", "López")
    luis = Profesor("Luis", "Martínez")
    clara = Profesor("Clara", "Torres")
    return ana, luis, clara

@pytest.fixture
def asignaturas():
    redes = Asignatura("Redes", "M03", "ASIX", "1º", 6)
    bd = Asignatura("BD", "M08", "DAW", "2º", 4)
    montaje = Asignatura("Montaje", "M01", "SMX", "1º", 3)
    return redes, bd, montaje

@pytest.fixture
def asignaturas_codocencia(profesores):
    ana, luis, _ = profesores

    redes = Asignatura("Redes Locales", "M03", "ASIX", "1º", 6)
    redes.asignar_profesor(ana, 3)
    redes.asignar_profesor(luis, 3)

    bd = Asignatura("Bases de Datos", "M08", "DAW", "2º", 5)
    bd.asignar_profesor(ana, 4)
    bd.asignar_profesor(luis, 1)

    smx = Asignatura("Montaje", "M01", "SMX", "1º", 3)  # sin asignar

    return [redes, bd, smx]

@pytest.fixture
def profesores_cargados():
    ana = Profesor("Ana", "López")
    luis = Profesor("Luis", "Martínez")

    # Asignaturas simuladas para cargar a Ana con el máximo permitido
    redes = Asignatura("Redes", "M03", "ASIX", "1º", 6)
    bd = Asignatura("Bases de Datos", "M08", "DAW", "2º", 6)
    sistemas = Asignatura("Sistemas", "M10", "ASIX", "2º", 6)

    redes.asignar_profesor(ana, 6)
    bd.asignar_profesor(ana, 6)
    sistemas.asignar_profesor(ana, 6)  # Total = 18

    return ana, luis
