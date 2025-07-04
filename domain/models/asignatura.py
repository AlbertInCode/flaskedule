class Asignatura:
    def __init__(self, nombre, modulo, ciclo, curso, horas):
        self.nombre = nombre
        self.modulo = modulo
        self.ciclo = ciclo
        self.curso = curso
        self.horas = horas
        self.distribucion = {}  # dict: profesor → horas

    def asignar_profesor(self, profesor, horas):
        self.distribucion[profesor] = horas
        if self not in profesor.asignaturas:
            profesor.asignaturas.append(self)

    def profesores(self):
        return list(self.distribucion.keys())

    def esta_asignada(self):
        return len(self.distribucion) > 0

    def horas_por_profesor(self, profesor):
        return self.distribucion.get(profesor, 0)

    def reparto_equilibrado(self):
        if not self.distribucion:
            return True
        cargas = list(self.distribucion.values())
        return max(cargas) - min(cargas) <= 1
