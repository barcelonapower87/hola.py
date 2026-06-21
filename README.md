# proyecto hola.py
# Sistema de Control de Acceso al Club 🚪🔞

Una aplicación sencilla e inteligente escrita en Python para gestionar el acceso de usuarios a un establecimiento, validando de forma automática si cumplen con la mayoría de edad requerida.

---

## 🚀 Características

* **Validación de Edad Automatizada:** Comprueba si el usuario tiene 18 años o más para permitir el ingreso.
* **Mensajes Personalizados Dinámicos:** El sistema adapta su respuesta de manera inteligente en función de los datos ingresados (ej. calcula con precisión el plural o singular de los años restantes si el usuario es menor).
* **Acceso a Zona VIP:** Incluye una verificación lógica condicional para otorgar beneficios especiales dentro del establecimiento.

---

## 🛠️ Estructura del Código

El script está organizado de manera limpia siguiendo las fases esenciales del desarrollo de software:
1.  **Definición de variables:** Configuración de los datos de prueba del usuario.
2.  **Preparación de datos:** Operaciones lógicas previas y cálculo de la diferencia de edad.
3.  **Procesamiento:** Lógica de decisión mediante estructuras condicionales (`if-else`).
4.  **Salida:** Formateo y presentación de los resultados finales en la consola.

---

## 💻 Requisitos y Uso

### Requisitos previos
* Tener instalado **Python 3.x** en tu equipo.

### Instrucciones de ejecución
1. Clona este repositorio o descarga el archivo `hola.py`.
2. Abre la terminal o consola de comandos en la carpeta donde guardaste el archivo.
3. Ejecuta el siguiente comando:

```bash
python hola.py

​Caso Mayor de Edad (Configuración actual: Juan, 18 años)

------------------------------
PROBANDO CON: Juan (18 años)
------------------------------
¡Bienvenido Juan! Puedes pasar al club.
Disfruta de la zona VIP.
------------------------------

Caso Menor de Edad (Si cambias la variable a: Juan, 17 años)

------------------------------
PROBANDO CON: Juan (17 años)
------------------------------
Lo siento Juan, eres menor. Vuelve en 1 año.
------------------------------
