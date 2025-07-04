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
