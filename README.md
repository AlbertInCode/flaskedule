# 🧑‍🏫 Gestor Docente - School Scheduler

Aplicación web para gestionar la asignación de profesores a módulos y ciclos formativos en centros educativos. Diseñada con los principios de Clean Code y Domain-Driven Design (DDD).

---

## 🧠 Filosofía del proyecto

- 🧩 **Clean Code**: código claro, nombres expresivos, funciones pequeñas y responsabilidades bien definidas.
- 🧭 **DDD**: el dominio educativo manda.

---

## 🚀 Cómo ejecutar el proyecto

### 🔧 Requisitos

- Python ≥ 3.8
- Flask

### 📦 Instalación

```bash
pip install flask
```

### ▶️ Lanzamiento

```bash
python app.py
```

Abre [http://localhost:5000](http://localhost:5000) en tu navegador.

---

## 🗂️ Estructura de carpetas

```
school_scheduler/
├── app.py
├── data/
│   ├── profesores.json
│   └── asignaturas.json
├── domain/
│   └── models/
│       ├── profesor.py
│       └── asignatura.py
├── infrastructure/
│   └── storage/
│       ├── json_loader.py
│       └── json_saver.py
├── interfaces/
│   ├── routes/
│   │   └── main.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── detalle_profesor.html
│       └── resumen.html
├── static/
│   └── style.css
```

---

## 📁 Datos iniciales

Los archivos `profesores.json` y `asignaturas.json` contienen datos de ejemplo. Puedes modificarlos libremente para adaptarlos a tu centro.

### profesores.json
```json
[
  { "nombre": "Ana", "apellido": "López", "tutor_de": null },
  { "nombre": "Luis", "apellido": "Martínez", "tutor_de": null },
  { "nombre": "Clara", "apellido": "Torres", "tutor_de": null }
]
```

### asignaturas.json
```json
[
  {
    "nombre": "Redes Locales",
    "modulo": "M03",
    "ciclo": "ASIX",
    "curso": "1º",
    "horas": 5,
    "profesores": ["Ana"]
  },
  {
    "nombre": "Bases de Datos",
    "modulo": "M08",
    "ciclo": "DAW",
    "curso": "2º",
    "horas": 4,
    "profesores": ["Luis"]
  },
  {
    "nombre": "Montaje de Equipos",
    "modulo": "M01",
    "ciclo": "SMX",
    "curso": "1º",
    "horas": 3,
    "profesores": []
  }
]
```

---

## 🧮 Funcionalidades clave

- 📋 Vista por profesor: asignaturas, carga horaria, grupo dominante
- 🏅 Nominar como tutor automáticamente
- 📚 Vista por asignaturas: edición, codocencia, reparto por horas
- 📈 Panel resumen: asignaturas sin cubrir, desbalances, estadísticas
- 📊 Gráficas interactivas por ciclo, módulo y curso

---

## 🛠️ Extensiones futuras (ideas)

- 🗃️ Conexión con base de datos (SQL)
- 🔑 Login para coordinación y docentes
- 📤 Exportación de informes en PDF o Excel
- 📅 Gestión de horarios y sesiones
