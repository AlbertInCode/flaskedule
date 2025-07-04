# models.py
class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.iniciales = f"{nombre[0]}{apellido[0]}".upper()
        self.horas_asignadas = 0
        self.asignaturas = []
        self.tutor_de = None

    def horas_restantes(self):
        return max(0, 18 - self.horas_asignadas)
    def grupo_dominante(self):
        grupos = {}
        for a in self.asignaturas:
            grupos[a.curso] = grupos.get(a.curso, 0) + a.horas
        if not grupos:
            return None
        curso_max = max(grupos, key=grupos.get)
        return curso_max, grupos[curso_max]


class Asignatura:
    def __init__(self, nombre, modulo, ciclo, curso, horas):
        self.nombre = nombre
        self.modulo = modulo
        self.ciclo = ciclo
        self.curso = curso
        self.horas = horas
        self.profesores = []

    def esta_asignada(self):
        return len(self.profesores) > 0

    def reparto_equilibrado(self):
        if not self.profesores or len(self.profesores) == 0:
            return None
        horas = [p.horas_asignadas for p in self.profesores]
        return max(horas) - min(horas) <= 1

