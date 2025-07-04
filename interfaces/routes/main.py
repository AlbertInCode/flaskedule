from flask import Blueprint, render_template, request, redirect, url_for
from models import Profesor, Asignatura
from utils import cargar_profesores, cargar_asignaturas, guardar_profesores, guardar_asignaturas

main = Blueprint('main', __name__)

profesores = cargar_profesores()
asignaturas = cargar_asignaturas(profesores=profesores)

@main.route('/')
def index():
    return render_template('index.html', profesores=profesores, asignaturas=asignaturas)

@main.route('/asignar/<int:idx>', methods=['GET', 'POST'])
def asignar_asignatura(idx):
    asignatura = asignaturas[idx]

    if request.method == 'POST':
        seleccionados = request.form.getlist('profesores')
        horas_por_profe = asignatura.horas // len(seleccionados)

        for nombre_profesor in seleccionados:
            profe = next((p for p in profesores if p.nombre == nombre_profesor), None)
            if profe and profe.horas_asignadas + horas_por_profe <= 18:
                asignatura.profesores.append(profe)
                profe.horas_asignadas += horas_por_profe
                profe.asignaturas.append(asignatura)

        guardar_profesores(profesores)
        guardar_asignaturas(asignaturas)


        return redirect(url_for('main.index'))

    return render_template('asignar.html', asignatura=asignatura, profesores=profesores)

@main.route('/resumen')
def resumen():
    sin_asignar = [a for a in asignaturas if not a.esta_asignada()]
    
    # Conteo por módulo
    modulo_stats = {}
    for a in asignaturas:
        if a.modulo not in modulo_stats:
            modulo_stats[a.modulo] = {"count": 0, "horas": 0}
        modulo_stats[a.modulo]["count"] += 1
        modulo_stats[a.modulo]["horas"] += a.horas

    modulos = list(modulo_stats.keys())
    modulo_counts = [modulo_stats[m]["count"] for m in modulos]
    modulo_horas = [modulo_stats[m]["horas"] for m in modulos]

    return render_template("resumen.html",
        profesores=profesores,
        asignaturas=asignaturas,
        sin_asignar=sin_asignar,
        modulos=modulos,
        modulo_counts=modulo_counts,
        modulo_horas=modulo_horas
    )


@main.route('/profesor/<nombre>')
def ver_profesor(nombre):
    profe = next((p for p in profesores if p.nombre == nombre), None)

    # Calcular distribución por curso
    cursos = {}
    for a in profe.asignaturas:
        cursos[a.curso] = cursos.get(a.curso, 0) + a.horas

    labels = list(cursos.keys())
    horas = list(cursos.values())

    return render_template("detalle_profesor.html", profe=profe, cursos=labels, horas_por_curso=horas)


@main.route('/nominar/<nombre>', methods=['POST'])
def nominar_tutor(nombre):
    profe = next((p for p in profesores if p.nombre == nombre), None)
    if profe and profe.grupo_dominante():
        profe.tutor_de = profe.grupo_dominante()[0]
        guardar_profesores(profesores)
    return redirect(url_for('main.ver_profesor', nombre=nombre))

@main.route('/asignaturas')
def vista_asignaturas():
    return render_template('asignaturas.html', asignaturas=asignaturas)

@main.route('/editar_asignatura/<int:idx>', methods=['GET', 'POST'])
def editar_asignatura(idx):
    asignatura = asignaturas[idx]
    if request.method == 'POST':
        seleccionados = request.form.getlist('profesores')
        distribucion = request.form.to_dict(flat=False).get('horas', [])

        # Limpiar asignación previa
        for profe in asignatura.profesores:
            profe.horas_asignadas -= asignatura.horas // len(asignatura.profesores)
            if asignatura in profe.asignaturas:
                profe.asignaturas.remove(asignatura)

        asignatura.profesores.clear()

        for i, nombre in enumerate(seleccionados):
            profe = next((p for p in profesores if p.nombre == nombre), None)
            h = int(distribucion[i]) if i < len(distribucion) else 0
            if profe and profe.horas_asignadas + h <= 18:
                profe.horas_asignadas += h
                profe.asignaturas.append(asignatura)
                asignatura.profesores.append(profe)

        guardar_profesores(profesores)
        guardar_asignaturas(asignaturas)
        return redirect(url_for('main.vista_asignaturas'))

    return render_template('editar_asignatura.html', asignatura=asignatura, profesores=profesores)

