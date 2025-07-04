from flask import Blueprint, render_template, request, redirect, url_for
from infrastructure.storage.json_loader import cargar_profesores, cargar_asignaturas
from infrastructure.storage.json_saver import guardar_profesores, guardar_asignaturas
from domain.services.asignacion import nominar_tutor
from application.orchestrator import asignar_profesor_a_asignatura, generar_resumen_general

main = Blueprint('main', __name__)

profesores = cargar_profesores()
asignaturas = cargar_asignaturas(profesores=profesores)

@main.route('/')
def index():
    return render_template('index.html', profesores=profesores)

@main.route('/profesor/<nombre>')
def ver_profesor(nombre):
    profe = next((p for p in profesores if p.nombre == nombre), None)
    cursos = {}
    for a in profe.asignaturas:
        cursos[a.curso] = cursos.get(a.curso, 0) + a.horas_por_profesor(profe)
    return render_template('detalle_profesor.html',
                           profe=profe,
                           cursos=list(cursos.keys()),
                           horas_por_curso=list(cursos.values()))

@main.route('/nominar/<nombre>', methods=['POST'])
def nominar(nombre):
    profe = next((p for p in profesores if p.nombre == nombre), None)
    nominar_como_tutor(profe)
    guardar_profesores(profesores)
    return redirect(url_for('main.ver_profesor', nombre=nombre))

@main.route('/resumen')
def resumen():
    resumen_info = generar_resumen_general(profesores, asignaturas)

    ciclo_count = {}
    modulo_count = {}
    for a in asignaturas:
        ciclo_count[a.ciclo] = ciclo_count.get(a.ciclo, 0) + 1
        modulo_count[a.modulo] = modulo_count.get(a.modulo, 0) + 1

    return render_template('resumen.html',
                           asignaturas=asignaturas,
                           profesores=profesores,
                           sin_asignar=resumen_info['sin_asignar'],
                           ciclos=list(ciclo_count.keys()),
                           ciclo_vals=list(ciclo_count.values()),
                           modulos=list(modulo_count.keys()),
                           modulo_vals=list(modulo_count.values()))

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

