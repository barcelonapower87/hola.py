# proyecto hola.py
# Sistema de Acceso y Gestión - Club de Fuerza Titán 🏋️‍♂️

Este proyecto es un Sistema de Gestión de Usuarios y Herramienta de Entrenamiento desarrollado en Python. Está diseñado para administrar un club deportivo con niveles de seguridad, gestión de base de datos y herramientas de cálculo físico, todo operado desde la terminal (CLI).

## 📌 Características Principales

* **Seguridad Multinivel:** * **Administrador:** Acceso restringido mediante PIN (1234) para operaciones críticas (Registrar, Ver base de datos, Eliminar).
    * **Usuario Final:** Cada socio crea su propia clave personalizada al registrarse.
* **Gestión de Base de Datos (CRUD Completo):**
    * **Crear:** Registro nuevo con ID aleatorio de 5 dígitos.
    * **Leer:** Visualización segura de la base de datos completa.
    * **Buscar:** Buscador inteligente por ID para consulta rápida.
    * **Borrar:** Función de baja de usuarios con protección administrativa.
* **Herramientas de Entrenamiento:**
    * **Calculadora 1RM:** Herramienta integrada para calcular el peso máximo teórico (repetición máxima) usando la fórmula de Epley.
* **Persistencia de Datos:** Todos los registros se guardan de forma local en `registros_club.txt`.
* **Diseño Orientado al Usuario:** Flujo de trabajo optimizado que cierra el sistema automáticamente tras transacciones de registro para garantizar la seguridad de los datos.

## 🛠️ Requisitos Técnicos

* **Lenguaje:** Python 3.x
* **Librerías:** Utiliza únicamente librerías estándar (`random`), sin dependencias externas.
* **Entorno:** Compatible con cualquier terminal de Windows, macOS o Linux.

## 🚀 Instrucciones de Ejecución

1. Asegúrate de tener Python instalado.
2. Descarga el archivo `hola.py`.
3. Abre tu terminal en la carpeta donde se encuentra el archivo.
4. Ejecuta el programa con el comando:
   ```bash
   python hola.py



