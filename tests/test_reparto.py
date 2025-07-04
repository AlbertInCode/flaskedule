from domain.models.profesor import Profesor
from domain.models.asignatura import Asignatura

def test_reparto_equilibrado_con_codocencia():
    ana = Profesor("Ana", "López")
    luis = Profesor("Luis", "Martínez")
    redes = Asignatura("Redes", "M03", "ASIX", "1º", 6)

    redes.asignar_profesor(ana, 3)
    redes.asignar_profesor(luis, 3)

    assert redes.reparto_equilibrado() is True

def test_reparto_desequilibrado():
    clara = Profesor("Clara", "Torres")
    jordi = Profesor("Jordi", "Blanc")
    bd = Asignatura("Bases de Datos", "M08", "DAW", "2º", 5)

    bd.asignar_profesor(clara, 4)
    bd.asignar_profesor(jordi, 1)

    assert bd.reparto_equilibrado() is False

def test_reparto_equilibrado_con_fixture(profesores, asignaturas):
    ana, luis, _ = profesores
    redes, _, _ = asignaturas

    redes.asignar_profesor(ana, 3)
    redes.asignar_profesor(luis, 3)

    assert redes.reparto_equilibrado() is True

def test_codocencia_equilibrada_y_desequilibrada(asignaturas_codocencia):
    redes, bd, smx = asignaturas_codocencia

    assert redes.reparto_equilibrado() is True
    assert bd.reparto_equilibrado() is False
    assert smx.esta_asignada() is False
