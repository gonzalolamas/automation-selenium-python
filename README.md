# 🚀 Automation Web con Selenium y Python

Pruebas automatizadas de sitios web utilizando **Selenium WebDriver** y **Python**, desarrolladas como parte del curso de automatización brindado por Arbusta.

---

## 🛠️ Tecnologías utilizadas

- **Python** — Lenguaje principal
- **Selenium WebDriver** — Automatización del navegador
- **Pytest** — Framework de testing
- **WebDriver Manager** — Gestión automática del driver

---

## 🌐 Sitios web automatizados

| Sitio | Descripción |
|---|---|
| [OrangeHRM](https://opensource-demo.orangehrmlive.com) | Sistema de gestión de recursos humanos |
| [Test.im](https://test.im) | Plataforma de pruebas web demo |

---

## ✅ Casos de prueba cubiertos

- 🔐 Login / autenticación de sesión
- 📋 Llenado de formularios
- 🔗 Manejo de links y navegación entre secciones
- ⚠️ Manejo de alertas (Alert.py)
- ☑️ Interacción con checkboxes (Test_box.py)
- 📜 Scroll en páginas (Test_scroll.py)
- 📂 Upload de archivos (Test_upload.py)
- 🔽 Selects y dropdowns (Test_select.py)
- ⏱️ Waits explícitos e implícitos
- ✅ Validación de texto en pantalla (Validar_texto.py)
- 🧱 Condicionales (Conditional.py)

---

## 📁 Estructura del proyecto

```
automation-selenium-python/
│
├── Practicas_PO/          # Prácticas con Page Object Model
├── Pytest/                # Tests organizados con Pytest
│
├── Alert.py
├── Base_Unnites.py
├── Conditional.py
├── Test_2.py
├── Test_3.py
├── Test_6_Keys.py
├── Test_Navegar.py
├── Test_box.py
├── Test_explicty_wait.py
├── Test_implicity_wait.py
├── Test_links.py
├── Test_scroll.py
├── Test_select.py
├── Test_select_try.py
├── Test_upload.py
└── Validar_texto.py
```

---

## ⚙️ Instalación y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/gonzalolamas/automation-selenium-python.git
cd automation-selenium-python
```

### 2. Instalar dependencias

```bash
pip install selenium pytest webdriver-manager
```

### 3. Ejecutar un test

```bash
python Test_2.py
```

### 4. Ejecutar tests con Pytest

```bash
cd Pytest
pytest
```

---

## 📚 Aprendizajes

Este proyecto me permitió practicar:

- Localización de elementos con CSS selectors, XPath, ID y Name
- Manejo de tiempos de espera para evitar fallos por carga dinámica
- Interacción con distintos tipos de elementos HTML
- Organización de pruebas con Pytest
- Primeros pasos con el patrón Page Object Model (POM)

---

## 👤 Autor

**Gonzalo Lamas**
QA Engineer | Test Automation en Progreso

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Gonzalo%20Lamas-blue?logo=linkedin)](https://www.linkedin.com/in/gonzalolamas)
[![GitHub](https://img.shields.io/badge/GitHub-gonzalolamas-black?logo=github)](https://github.com/gonzalolamas)
