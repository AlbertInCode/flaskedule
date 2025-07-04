from domain.models.profesor import Profesor
from domain.models.asignatura import Asignatura
from domain.services.asignacion import nominar_tutor

def test_nominar_tutor_por_carga_mayor():
    ana = Profesor("Ana", "López")
    redes = Asignatura("Redes", "M03", "ASIX", "1º", 5)
    bd = Asignatura("BD", "M08", "DAW", "2º", 3)

    redes.asignar_profesor(ana, 5)
    bd.asignar_profesor(ana, 3)

    nominar_tutor(ana)

    assert ana.tutor_de == "1º"

def test_tutor_null_si_sin_asignaturas():
    luis = Profesor("Luis", "Martínez")
    nominar_tutor(luis)
    assert luis.tutor_de is None
