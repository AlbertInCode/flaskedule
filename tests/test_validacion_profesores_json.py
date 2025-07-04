import json
from config import PROFESORES_FILE

def test_profesores_json_es_valido():
    with open(PROFESORES_FILE) as f:
        data = json.load(f)

    nombres_vistos = set()

    for profe in data:
        # Verifica que tiene las claves necesarias
        assert "nombre" in profe
        assert "apellido" in profe
        #assert "tutor_de" in profe

        nombre = profe["nombre"]
        assert nombre not in nombres_vistos, f"Duplicado detectado: {nombre}"
        nombres_vistos.add(nombre)
