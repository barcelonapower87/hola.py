# proyecto hola.py
# Sistema de Acceso Interactivo - Club de Fuerza Titán 🏋️‍♂️

Un programa de consola (CLI) desarrollado en Python para gestionar el registro, acceso y facturación de usuarios en un club deportivo. Este sistema está diseñado con un fuerte enfoque en la **Experiencia de Usuario (UX)**, la validación estricta de datos y la persistencia de información.

## 📌 Características Principales

* **Generación de ID Único (Nuevo):** El sistema asigna automáticamente una etiqueta de socio aleatoria de 5 dígitos a cada nuevo cliente para facilitar su identificación en la base de datos.
* **Flujo Transaccional Seguro (Nuevo):** Al procesar un nuevo registro y finalizar la oferta comercial (VIP o Estándar), el sistema se cierra automáticamente para garantizar la seguridad de la transacción, emulando un punto de venta real.
* **Persistencia de Datos:** Los registros exitosos se guardan automáticamente en un archivo local (`registros_club.txt`) incluyendo el ID generado, nombre, edad y tipo de pase adquirido.
* **Menú Principal Interactivo:** Cuenta con una pantalla de inicio que permite al operador decidir si desea registrar a un nuevo cliente, consultar la base de datos de registros anteriores o salir del sistema.
* **Validación Estricta de Entradas:** * Verifica que el nombre contenga exclusivamente letras y espacios (bloqueando campos vacíos y números).
  * Protege la entrada de la edad contra errores de tipografía usando manejo de excepciones (`ValueError`).
* **Lógica Comercial (Upselling):** Ofrece un pase VIP dinámico exclusivamente a los usuarios que ya cumplieron con los requisitos mínimos de edad (18+).

## 🛠️ Requisitos del Sistema

* **Python 3.6** o superior.
* Ejecución nativa (No requiere la instalación de bibliotecas externas, solo utiliza librerías estándar como `os` y `random`).

## 🚀 Instrucciones de Ejecución

1. Asegúrate de tener Python instalado en tu equipo.
2. Descarga el archivo principal del programa llamado `hola.py`.
3. Abre tu terminal o línea de comandos. **Es indispensable que inicies la terminal exactamente en la misma ruta/carpeta donde guardaste `hola.py`.**
4. Ejecuta el programa con el siguiente comando:

   ```bash
   python hola.py


