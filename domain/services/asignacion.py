def nominar_tutor(profesor):
    grupo, horas = profesor.grupo_dominante()
    return {"nombre": profesor.nombre, "grupo": grupo, "horas": horas}
