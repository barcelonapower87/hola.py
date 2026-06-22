import random

# ==============================================================================
# CONFIGURACIÓN DE SEGURIDAD
# ==============================================================================
PIN_ADMINISTRADOR = "1234"

def verificar_admin():
    """Pide la contraseña antes de permitir acciones administrativas."""
    print("\n[🔒 ACCESO RESTRINGIDO]")
    intento = input("▶ Ingresa el PIN de Administrador: ").strip()
    if intento == PIN_ADMINISTRADOR:
        return True
    else:
        print("  ❌ PIN incorrecto. Acceso denegado.")
        return False

# ==============================================================================
# FUNCIONES DE BASE DE DATOS (Guardar, Leer, Buscar y Eliminar)
# ==============================================================================

def guardar_registro(id_socio, nombre, edad, es_vip, clave_usuario):
    """Guarda los datos del cliente en un archivo txt."""
    tipo_pase = "VIP" if es_vip else "Estándar"
    try:
        with open("registros_club.txt", "a", encoding="utf-8") as archivo:
            # Ahora dice "Clave" en lugar de "PIN" para que tenga sentido si escriben letras
            archivo.write(f"ID: #{id_socio} | Nombre: {nombre} | Edad: {edad} | Pase: {tipo_pase} | Clave: {clave_usuario}\n")
        print("💾 [Registro guardado exitosamente en la base de datos]")
    except OSError:
        print("⚠️ [Aviso del Sistema]: Dispositivo bloqueó la escritura del archivo.")

def ver_registros_guardados():
    if not verificar_admin():
        return

    print("\n--------------------------------------------------")
    print("             BASE DE DATOS DEL CLUB               ")
    print("--------------------------------------------------")
    try:
        with open("registros_club.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido.strip() == "":
                print("El archivo está vacío. No hay clientes registrados aún.")
            else:
                print(contenido)
    except FileNotFoundError:
        print("⚠️ Aún no se ha creado la base de datos. Registra a un cliente primero.")
    print("--------------------------------------------------")

def buscar_cliente():
    print("\n--- BUSCADOR INTELIGENTE ---")
    id_buscado = input("▶ Ingresa el ID de 5 dígitos a buscar (ej. 48291): ").strip()
    
    try:
        encontrado = False
        with open("registros_club.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if f"ID: #{id_buscado}" in linea:
                    print("\n✅ Cliente encontrado:")
                    print(f"   {linea.strip()}")
                    encontrado = True
                    break
                    
        if not encontrado:
            print(f"\n❌ No se encontró ningún cliente con el ID #{id_buscado}.")
            
    except FileNotFoundError:
        print("⚠️ La base de datos está vacía. No hay a quién buscar.")

def eliminar_cliente():
    print("\n--- DAR DE BAJA A UN CLIENTE ---")
    if not verificar_admin():
        return
        
    id_borrar = input("▶ Ingresa el ID del cliente que deseas eliminar: ").strip()
    
    try:
        with open("registros_club.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            
        with open("registros_club.txt", "w", encoding="utf-8") as archivo:
            borrado = False
            for linea in lineas:
                if f"ID: #{id_borrar}" not in linea:
                    archivo.write(linea)
                else:
                    borrado = True
                    
        if borrado:
            print(f"\n✅ El cliente con ID #{id_borrar} ha sido eliminado del sistema.")
        else:
            print(f"\n❌ No se encontró ningún cliente con el ID #{id_borrar}.")
            
    except FileNotFoundError:
        print("⚠️ La base de datos está vacía.")

# ==============================================================================
# HERRAMIENTAS PARA ATLETAS
# ==============================================================================

def calculadora_1rm():
    print("\n--- CALCULADORA DE FUERZA MÁXIMA (1RM) ---")
    print("Descubre cuál es tu peso máximo teórico para una sola repetición.")
    try:
        peso = float(input("▶ Ingresa el peso que levantaste (en kg o lbs): ").strip())
        reps = int(input("▶ Ingresa cuántas repeticiones lograste con ese peso: ").strip())
        
        if reps <= 0 or peso <= 0:
            print("  ⚠️ Error: Los valores deben ser mayores a cero.")
            return
            
        rm = peso * (1 + (0.0333 * reps))
        
        print("\n💪 RESULTADO DE TU EVALUACIÓN:")
        print(f"   Tu repetición máxima estimada es de: {rm:.2f}")
        print("   ¡Excelente trabajo estructural y de fuerza!")
        
    except ValueError:
        print("  ⚠️ Error: Por favor ingresa solo números (ej. 80.5 o 10).")

# ==============================================================================
# FUNCIÓN DE REGISTRO
# ==============================================================================

def registrar_cliente():
    if not verificar_admin():
        return False

    print("\n--- Nuevo Cliente ---")
    
    print("\n[?] Necesitamos tu nombre para personalizar tu pase de acceso físico.")
    while True:
        nombre = input("▶ Ingresa el nombre del cliente: ").strip()
        if not nombre:
            print("  ⚠️ Error: El nombre no puede estar vacío.")
        elif not nombre.replace(" ", "").isalpha():
            print("  ⚠️ Error: El nombre solo debe contener letras.")
        else:
            break
            
    print("\n[?] Solicitamos tu edad por motivos de seguridad. Mínimo 18 años.")
    edad = -1
    while edad < 0:
        try:
            edad = int(input("▶ Ingresa la edad en números (ej. 20): ").strip())
            if edad < 0 or edad > 120:
                print("  ⚠️ Error: Ingresa una edad válida.")
                edad = -1
        except ValueError:
            print("  ⚠️ Error: Has ingresado texto. Usa solo números enteros.")
            
    print("\n--------------------------------------------------")
    if edad >= 18:
        print(f"✅ Requisitos cumplidos, {nombre}.")
        print("\n[?] OFERTA OPCIONAL: Pase VIP por $50 adicionales.")
        
        es_vip = False
        while True:
            respuesta = input("▶ ¿Deseas adquirir la entrada VIP? (s/n): ").strip().lower()
            if respuesta in ['s', 'si', 'sí']:
                es_vip = True
                break
            elif respuesta in ['n', 'no']:
                break
            else:
                print("  ⚠️ Por favor, responde solo con 's' (Sí) o 'n' (No).")
                
        id_socio = random.randint(10000, 99999)
                
        print("\n--------------------------------------------------")
        if es_vip:
            print(f"🌟 ¡Bienvenido a la experiencia VIP, {nombre}!")
        else:
            print(f"✅ ¡Registro estándar exitoso! Bienvenido, {nombre}.")
            
        print(f"   Tu Etiqueta de socio Titán es: #{id_socio}")

        # NUEVO: Libertad total para la clave
        print("\n[?] Crea una clave de seguridad para tu cuenta (letras, números o lo que quieras).")
        while True:
            clave_usuario = input("▶ Ingresa tu nueva clave: ").strip()
            # Mientras no lo deje completamente en blanco, el programa lo acepta
            if clave_usuario != "":
                print("  ✅ Clave configurada exitosamente.")
                break
            else:
                print("  ⚠️ Error: La clave no puede estar vacía. Inténtalo de nuevo.")

        guardar_registro(id_socio, nombre, edad, es_vip, clave_usuario)
        
    else:
        print(f"❌ Acceso denegado. Lo sentimos, {nombre}.")
        print(f"   Actualmente tienes {edad} años. No cumples el mínimo requerido.")
    print("--------------------------------------------------")
    return True

# ==============================================================================
# MOTOR DEL PROGRAMA: EL MENÚ PRINCIPAL
# ==============================================================================

def menu_principal():
    while True:
        print("\n==================================================")
        print("    SISTEMA DE ACCESO - CLUB DE FUERZA TITÁN      ")
        print("==================================================")
        print("  [1] Registrar nuevo cliente (Requiere PIN de Admin)")
        print("  [2] Calculadora de Repetición Máxima (1RM)")
        print("  [3] Buscar a un cliente por número de ID")
        print("  [4] Ver todos los registrados (Requiere PIN de Admin)")
        print("  [5] Eliminar a un cliente (Requiere PIN de Admin)")
        print("  [6] Salir del sistema")
        print("==================================================")
        
        opcion = input("▶ Ingresa el número de tu opción (1-6): ").strip()
        
        if opcion == '1':
            if registrar_cliente():
                print("\n==================================================")
                print("  TRANSACCIÓN FINALIZADA. CERRANDO EL SISTEMA...")
                print("==================================================")
                break 
            
        elif opcion == '2':
            calculadora_1rm()
            
        elif opcion == '3':
            buscar_cliente()
            
        elif opcion == '4':
            ver_registros_guardados()
            
        elif opcion == '5':
            eliminar_cliente()
            
        elif opcion == '6':
            print("\nCerrando el sistema de forma segura. ¡Hasta luego!")
            break 
            
        else:
            print("\n⚠️ Error: Opción no válida. Por favor, ingresa un número del 1 al 6.")

if __name__ == "__main__":
    menu_principal()

