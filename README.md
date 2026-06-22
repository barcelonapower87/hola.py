# proyecto hola.py
# Sistema de Acceso y Gestión - Club de Fuerza Titán 🏋️‍♂️

Este proyecto es un Sistema de Gestión de Usuarios y Herramienta de Entrenamiento desarrollado en Python. Está diseñado para administrar un club deportivo con niveles de seguridad, gestión de base de datos en tiempo real y herramientas de cálculo físico, todo operado desde la terminal (CLI).

## 📌 Características Principales

* **Flujo de Trabajo Continuo (NUEVO):** El sistema mantiene un ciclo de ejecución infinito, permitiendo al operador registrar múltiples clientes, realizar búsquedas o hacer cálculos sin necesidad de reiniciar el programa tras cada transacción.
* **Seguridad Multinivel:** * **Administrador:** Acceso restringido mediante PIN maestro (1234) para proteger operaciones críticas (Registrar, Ver base de datos, Eliminar).
    * **Usuario Final:** Durante el registro, cada socio configura su propia clave de seguridad alfanumérica personalizada.
* **Gestión de Base de Datos (CRUD Completo):**
    * **Crear:** Registro nuevo con ID aleatorio automático de 5 dígitos.
    * **Leer:** Visualización segura de la base de datos completa.
    * **Buscar:** Buscador inteligente por ID para consulta rápida de clientes.
    * **Borrar:** Función de baja de usuarios con protección administrativa, que reescribe el archivo de forma segura.
* **Herramientas de Entrenamiento:**
    * **Calculadora 1RM:** Herramienta integrada para calcular el peso máximo teórico (repetición máxima) usando la fórmula de Epley.
* **Persistencia de Datos:** Todos los registros se guardan de forma local en `registros_club.txt` previniendo la pérdida de información.

## 🛠️ Requisitos Técnicos

* **Lenguaje:** Python 3.x
* **Librerías:** Utiliza únicamente librerías estándar nativas (`random`), sin requerir instalaciones de terceros.
* **Entorno:** Compatible con cualquier terminal de Windows, macOS o Linux.

## 🚀 Instrucciones de Ejecución

1. Asegúrate de tener Python instalado en el sistema.
2. Descarga el archivo principal `hola.py`.
3. Abre tu terminal o línea de comandos en el directorio donde se encuentra el archivo.
4. Ejecuta el programa con el comando:
   ```bash
   python hola.py


