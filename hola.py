import random 

# ==============================================================================
# FUNCIONES DE BASE DE DATOS (Guardar y Leer)
# ==============================================================================

def guardar_registro(id_socio, nombre, edad, es_vip):
    """Guarda los datos del cliente en un archivo txt."""
    tipo_pase = "VIP" if es_vip else "Estándar"
    try:
        with open("registros_club.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"ID: #{id_socio} | Nombre: {nombre} | Edad: {edad} | Pase: {tipo_pase}\n")
        print("💾 [Registro guardado exitosamente en la base de datos]")
    except OSError:
        print("⚠️ [Aviso del Sistema]: El registro se procesó, pero el dispositivo bloqueó la escritura del archivo.")

def ver_registros_guardados():
    """Lee el archivo txt y lo muestra en la consola"""
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

# ==============================================================================
# FUNCIÓN DE REGISTRO (Con validación estricta)
# ==============================================================================

def registrar_cliente():
    print("\n--- Nuevo Cliente ---")
    
    # 1. Validación del nombre
    print("\n[?] Necesitamos tu nombre para personalizar tu pase de acceso físico.")
    while True:
        nombre = input("▶ Ingresa el nombre del cliente: ").strip()
        if not nombre:
            print("  ⚠️ Error: El nombre no puede estar vacío.")
        elif not nombre.replace(" ", "").isalpha():
            print("  ⚠️ Error: El nombre solo debe contener letras (sin números ni símbolos).")
        else:
            break
            
    # 2. Validación de la edad
    print("\n[?] Solicitamos tu edad por motivos de seguridad. Nuestras instalaciones exigen un mínimo de 18 años.")
    edad = -1
    while edad < 0:
        try:
            edad = int(input("▶ Ingresa la edad en números (ej. 20): ").strip())
            if edad < 0 or edad > 120:
                print("  ⚠️ Error: Ingresa una edad válida.")
                edad = -1
        except ValueError:
            print("  ⚠️ Error: Has ingresado texto. Usa solo números enteros.")
            
    # 3. Lógica del Club y Guardado
    print("\n--------------------------------------------------")
    if edad >= 18:
        print(f"✅ Requisitos cumplidos, {nombre}.")
        print("\n[?] OFERTA OPCIONAL: Pase VIP por $50 adicionales.")
        print("    Beneficios: Sin fila de espera, acceso a la zona de spa, y batidos de cortesía.")
        
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
                
        # AQUÍ ESTÁ EL CAMBIO: Generamos el número aleatorio de 5 dígitos
        id_socio = random.randint(10000, 99999)
                
        print("\n--------------------------------------------------")
        if es_vip:
            print(f"🌟 ¡Bienvenido a la experiencia VIP, {nombre}!")
            print(f"   Tu Etiqueta de socio Titán es: #{id_socio}")
        else:
            print(f"✅ ¡Registro estándar exitoso! Bienvenido, {nombre}.")
            print(f"   Tu Etiqueta de socio es: #{id_socio}")
            
        guardar_registro(id_socio, nombre, edad, es_vip)
        
    else:
        print(f"❌ Acceso denegado. Lo sentimos, {nombre}.")
        print(f"   Actualmente tienes {edad} años. Por políticas del club,")
        print("   no podemos permitirte el acceso a las instalaciones aún.")
    print("--------------------------------------------------")

# ==============================================================================
# MOTOR DEL PROGRAMA: EL MENÚ PRINCIPAL
# ==============================================================================

def menu_principal():
    """Bucle infinito que mantiene el programa vivo y controla la navegación"""
    while True:
        print("\n==================================================")
        print("    SISTEMA DE ACCESO - CLUB DE FUERZA TITÁN      ")
        print("==================================================")
        print("Selecciona una opción del menú:")
        print("  [1] Registrar nuevo cliente")
        print("  [2] Ver base de datos de registrados")
        print("  [3] Salir del sistema")
        print("==================================================")
        
        opcion = input("▶ Ingresa el número de tu opción (1-3): ").strip()
        
        if opcion == '1':
            registrar_cliente()
            print("\n==================================================")
            print("  TRANSACCIÓN FINALIZADA. CERRANDO EL SISTEMA...")
            print("==================================================")
            break 
            
        elif opcion == '2':
            ver_registros_guardados()
            
        elif opcion == '3':
            print("\nCerrando el sistema de forma segura. ¡Hasta luego!")
            break 
            
        else:
            print("\n⚠️ Error: Opción no válida. Por favor, ingresa 1, 2 o 3.")

# Punto de inicio
if __name__ == "__main__":
    menu_principal()
