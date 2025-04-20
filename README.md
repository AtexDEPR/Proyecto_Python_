# SISGESA - Sistema de Gestión de Asistencia Académica

**SISGESA** es una aplicación de consola desarrollada en Python bajo el paradigma estructurado. Su objetivo es automatizar el registro y control de la asistencia académica en instituciones educativas, mejorando los procesos administrativos y académicos mediante el uso de archivos JSON y seguridad con SHA-256.

## 📌 Características Principales

- 🔐 Inicio de sesión con verificación y encriptación SHA-256
- 🧾 Menú interactivo con múltiples opciones
- 👥 Registro y gestión de estudiantes, docentes, grupos y módulos
- 📅 Registro de asistencias con fecha y hora
- 🔍 Consultas por código (grupos, módulos, estudiantes y docentes)
- 📊 Generación de informes detallados por mes
- 💾 Persistencia de datos mediante archivos JSON
- ⚙️ Cambio de contraseña y validación robusta
- ❌ Manejo de errores para evitar interrupciones

## 📁 Estructura del Proyecto

```
SISGESA/
├── main.py
├── modulos/
│   ├── usuarios.py
│   ├── estudiantes.py
│   ├── docentes.py
│   └── ...
├── utils/
│   ├── seguridad.py
│   └── validaciones.py
├── data/
│   ├── estudiantes.json
│   ├── docentes.json
│   └── ...
```

## ▶️ Ejecución

```bash
python main.py
```

## 🧠 Requisitos Técnicos

- Python 3.x
- No requiere librerías externas
- Compatible con Windows, macOS y Linux

## 📚 Licencia

Proyecto desarrollado con fines académicos para **Campuslands - 2025**.

