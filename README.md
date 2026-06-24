# proyecto hola.py
# Sistema de Gestión - Club de Fuerza Titán 🏋️‍♂️

Software profesional desarrollado en Python bajo el paradigma de **Programación Orientada a Objetos (POO)**. Diseñado para la administración de un centro deportivo, integrando gestión de membresías, estrategias de venta y gamificación del entrenamiento.

## 🚀 Valor Agregado y Estrategia Comercial
Este sistema no solo almacena datos, sino que está pensado para generar comunidad y rentabilidad en el club:
* **Flujo de Conversión VIP:** El sistema ofrece automáticamente "Upgrades" a membresía VIP, destacando beneficios como la **Sala Privada** (máquinas tecnológicas) y el beneficio de ingresar hasta **2 invitados gratis**.
* **Gamificación (Tablero de Titanes 🏆):** Durante el registro, el sistema evalúa la fuerza base del atleta calculando su Repetición Máxima (1RM). Con estos datos, el software genera automáticamente un Ranking (Leaderboard) para fomentar la competencia amistosa y motivar a los usuarios.

## 📌 Características Principales
* **Arte ASCII y UX Limpia:** Interfaz de consola atractiva con el logo del club al iniciar y menús intuitivos sin sobrecarga visual.
* **Arquitectura Modular (POO):** Todo el núcleo lógico está estructurado y protegido dentro de la clase `SistemaClub`.
* **Seguridad Dinámica:** Sin contraseñas "quemadas" en el código. El Socio Principal configura sus credenciales en el primer arranque para proteger los datos de todos los clientes.
* **Gestión de Base de Datos (CRUD):** Registro completo, buscador inteligente, visualización y sistema de bajas, con guardado persistente local en formato `.txt`.
* **Calculadora de Fuerza Libre:** Módulo matemático independiente basado en la fórmula de Epley para que cualquier usuario calcule su 1RM.

## 🛠️ Requisitos Técnicos
* **Lenguaje:** Python 3.x
* **Estructura:** Código modular (`class SistemaClub`).
* **Librerías:** Utiliza únicamente la librería estándar nativa (`random`), garantizando portabilidad sin necesidad de instalar dependencias externas.

## 🚀 Instrucciones de Ejecución
1. Ejecuta el archivo principal desde tu consola o terminal:
   ```bash
   python hola.py