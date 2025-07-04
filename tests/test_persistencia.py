import os
import json
from infrastructure.storage.json_saver import guardar_profesores, guardar_asignaturas
from infrastructure.storage.json_loader import cargar_profesores, cargar_asignaturas
from domain.models.profesor import Profesor
from domain.models.asignatura import Asignatura
from config import PROFESORES_FILE, ASIGNATURAS_FILE

def test_guardar_y_cargar_datos_temporales(tmp_path):
    # Crear ruta temporal
    profesores_path = tmp_path / "profesores.json"
    asignaturas_path = tmp_path / "asignaturas.json"

    # Crear profesor y asignatura
    ana = Profesor("Ana", "López")
    redes = Asignatura("Redes Locales", "M03", "ASIX", "1º", 6)
    redes.asignar_profesor(ana, 6)

    # Guardar en disco
    guardar_profesores([ana], path=str(profesores_path))
    guardar_asignaturas([redes], path=str(asignaturas_path))

    # Cargar desde disco
    profesores = cargar_profesores(path=str(profesores_path))
    asignaturas = cargar_asignaturas(path=str(asignaturas_path), profesores=profesores)

    # Verificar que se mantuvieron los vínculos
    assert len(profesores) == 1
    assert len(asignaturas) == 1
    profe = profesores[0]
    asignatura = asignaturas[0]

    assert asignatura.nombre == "Redes Locales"
    assert profe.nombre == "Ana"
    assert asignatura.esta_asignada()
    assert profe.horas_asignadas == 6
