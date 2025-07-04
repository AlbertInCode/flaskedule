def nominar_tutor(profesor):
    grupo, horas = profesor.grupo_dominante()
    profesor.tutor_de = grupo
    return {"nombre": profesor.nombre, "grupo": grupo, "horas": horas}
