# proyecto hola.py
# Sistema de Acceso y Gestión - Club de Fuerza Titán 🏋️‍♂️

Este proyecto es un **Sistema de Gestión de Usuarios y Herramienta de Entrenamiento** desarrollado en Python. Ha sido construido utilizando **Programación Orientada a Objetos (POO)**, lo que garantiza un código modular, seguro y altamente mantenible.

## 📌 Características Principales

* **Arquitectura Orientada a Objetos:** El sistema está encapsulado en la clase `SistemaClub`, eliminando el uso de variables globales y mejorando la seguridad y organización de los datos.
* **Asistente de Configuración Inicial:** Al ejecutar el programa, el sistema guía al usuario a través de un "Setup Wizard" para configurar su cuenta de **Socio Principal**.
* **Seguridad Dinámica:** No existen contraseñas predefinidas en el código. La seguridad se basa en la clave que el usuario configura al arrancar el sistema, protegiendo las operaciones críticas.
* **Gestión de Base de Datos (CRUD Completo):**
    * **Crear:** Registro de nuevos clientes con ID aleatorio de 5 dígitos y asignación de tipo de pase (VIP/Estándar).
    * **Leer:** Visualización de registros protegida por la clave del Socio Principal.
    * **Buscar:** Buscador inteligente por ID para consulta rápida.
    * **Eliminar:** Función de baja de usuarios con protección de seguridad.
* **Herramientas de Entrenamiento:**
    * **Calculadora 1RM:** Herramienta integrada para calcular el peso máximo teórico (repetición máxima) usando la fórmula de Epley.
* **Persistencia de Datos:** Todos los registros se guardan localmente en `registros_club.txt` para asegurar que la información persista entre sesiones.

## 🛠️ Requisitos Técnicos

* **Lenguaje:** Python 3.x
* **Estructura:** Código modular basado en clases (`class SistemaClub`).
* **Librerías:** Utiliza únicamente la librería estándar nativa (`random`), sin dependencias externas.

## 🚀 Instrucciones de Ejecución

1. Asegúrate de tener Python instalado en tu sistema.
2. Descarga el archivo principal `hola.py`.
3. Abre tu terminal en la carpeta donde se encuentra el archivo.
4. Ejecuta el programa con el comando:
   ```bash
   python hola.py


