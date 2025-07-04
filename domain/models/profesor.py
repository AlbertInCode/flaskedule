class Profesor:
    MAX_HORAS = 18

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.iniciales = f"{nombre[0]}{apellido[0]}".upper()
        self.asignaturas = []

    @property
    def horas_asignadas(self):
        return sum(a.horas_por_profesor(self) for a in self.asignaturas)

    def horas_disponibles(self):
        return max(0, self.MAX_HORAS - self.horas_asignadas)

    def grupo_dominante(self):
        carga_por_grupo = {}
        for a in self.asignaturas:
            carga_por_grupo[a.curso] = carga_por_grupo.get(a.curso, 0) + a.horas_por_profesor(self)
        if not carga_por_grupo:
            return None
        curso = max(carga_por_grupo, key=carga_por_grupo.get)
        return curso, carga_por_grupo[curso]

    def asignar_asignatura(self, asignatura, horas):
        if self.horas_disponibles() >= horas:
            self.asignaturas.append(asignatura)
            asignatura.asignar_profesor(self, horas)
