# proyecto hola.py
# Sistema de Acceso Interactivo - Club de Fuerza 🏋️‍♂️

Un programa de consola (CLI) desarrollado en Python para gestionar el registro y acceso de usuarios a un club deportivo. Este sistema está diseñado con un fuerte enfoque en la **Experiencia de Usuario (UX)**, la validación estricta de datos y la persistencia de información.

## 📌 Características Principales

* **Persistencia de Datos (Nuevo):** Los registros exitosos se guardan automáticamente en un archivo local (`hola.txt`), asegurando que la información no se pierda al cerrar el programa y sirviendo como una base de datos real.
* **Validación Estricta de Entradas (Nuevo):** * El sistema verifica que el nombre de usuario contenga exclusivamente letras y espacios (rechazando números, símbolos o campos vacíos).
  * La edad está protegida contra errores de tipografía (manejo de excepciones `ValueError`).
* **Transparencia Activa:** El programa le explica al usuario el *por qué* de cada solicitud de datos antes de pedirla, generando confianza y evitando confusiones.
* **Flujo de Ejecución Continuo:** Permite registrar a múltiples clientes en bucle sin necesidad de reiniciar el script.
* **Lógica Comercial (Upselling):** Ofrece un pase VIP dinámico (con precio y beneficios detallados) exclusivamente a los usuarios que ya cumplieron con los requisitos mínimos de acceso.

## 🛠️ Requisitos del Sistema

* **Python 3.6** o superior.
* Ejecución nativa (No requiere la instalación de bibliotecas externas).

## 🚀 Instrucciones de Ejecución

1. Asegúrate de tener Python instalado en tu equipo.
2. Guarda el script principal en una carpeta (por ejemplo, `registro_club.py`).
3. Abre tu terminal o línea de comandos. **Es muy importante que navegues e inicies la terminal exactamente en la misma carpeta donde guardaste el archivo.**
4. Ejecuta el programa con el siguiente comando:

   ```bash
   python hola.py






