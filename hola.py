import random
import os  # <-- NUEVO: Para que el sistema revise los archivos por ti

class SistemaClub:
    def __init__(self):
        self.clave_maestra = ""
        self.nombre_socio_principal = ""
        self.edad_socio_principal = 0
        self.socio_principal_vip = False
        self.invitados_principal = 0

    # ==========================================================================
    # 1. SEGURIDAD Y CONFIGURACIÓN DEL SOCIO PRINCIPAL
    # ==========================================================================
    def configuracion_inicial(self):
        print("\n==================================================")
        print("  BIENVENIDO - CONFIGURAR SOCIO PRINCIPAL        ")
        print("==================================================")
        
        # --- MAGIA: LIMPIEZA AUTOMÁTICA DE BASE DE DATOS ---
        if os.path.exists("registros_club.txt"):
            print("  [!] El sistema detectó registros de pruebas anteriores.")
            limpiar = input("  ▶ ¿Deseas formatear la base de datos para empezar limpio? (s/n): ").strip().lower()
            if limpiar == 's':
                with open("registros_club.txt", "w", encoding="utf-8") as f:
                    f.write("") # Esto borra absolutamente todo
                print("  ✅ Base de datos formateada. El sistema está como nuevo.\n")
            else:
                print("  👍 Manteniendo los registros anteriores.\n")
        
        while True:
            nombre = input("▶ Ingresa tu nombre: ").strip()
            if nombre != "" and nombre.replace(" ", "").isalpha():
                self.nombre_socio_principal = nombre
                break
            else:
                print("  ⚠️ Error: Ingresa un nombre válido (solo letras).")
                
        while True:
            try:
                edad = int(input("▶ Ingresa tu edad (mínimo 18): "))
                if edad >= 18:
                    self.edad_socio_principal = edad
                    break
                else:
                    print("  ❌ Acceso denegado: Debes ser mayor de edad para administrar el club.")
            except ValueError:
                print("  ⚠️ Error: Ingresa una edad válida (solo números).")
                
        id_principal = random.randint(10000, 99999)
        print(f"\n✅ ¡Cuenta creada! Tu Etiqueta de socio Titán es: #{id_principal}")
        
        while True:
            self.clave_maestra = input(f"\n[?] {self.nombre_socio_principal}, crea tu clave de seguridad: ").strip()
            if self.clave_maestra != "":
                print("  ✅ Clave de seguridad configurada con éxito.")
                break

        print("\n--- EVALUACIÓN DE FUERZA INICIAL ---")
        print("Registremos tu marca personal para el Tablero de Titanes.")
        try:
            peso = float(input("▶ Peso máximo levantado (kg/lbs): "))
            reps = int(input("▶ Repeticiones logradas con ese peso: "))
            fuerza_1rm_principal = peso * (1 + (0.0333 * reps)) if peso > 0 and reps > 0 else 0.0
            print(f"💪 Tu 1RM ha sido registrado: {fuerza_1rm_principal:.2f}")
        except ValueError:
            print("  ⚠️ Datos inválidos. Se registrará 0.00 de fuerza base.")
            fuerza_1rm_principal = 0.0

        print("\n==================================================")
        print(" 🔥 ¡ESPERA! TENEMOS UNA OFERTA EXCLUSIVA PARA TI 🔥")
        print("==================================================")
        print(f"  Hola, {self.nombre_socio_principal}. Tu cuenta estándar ya está activa,")
        print("  pero... ¿por qué conformarte con lo ordinario?")
        print("\n  👑 ¡MEJORA TU MEMBRESÍA AL PASE VIP TITÁN! 👑")
        print("  ------------------------------------------------")
        print("  🚪 ACCESO EXCLUSIVO A LA SALA PRIVADA VIP")
        print("     Un espacio reservado solo para atletas de élite.")
        print("\n  🤖 MÁQUINAS CON TECNOLOGÍA DE ÚLTIMA GENERACIÓN")
        print("     Equipamiento inteligente que optimiza tus repeticiones.")
        print("\n  🤝 ¡NUEVO! PASE MULTI-INVITADO")
        print("     Como VIP, podrás traer hasta 10 acompañantes contigo, ¡GRATIS!")
        print("==================================================")
        
        oferta = input("▶ ¿Deseas ascender a Miembro VIP ahora mismo? (s/n): ").strip().lower()
        if oferta == 's':
            self.socio_principal_vip = True
            print("\n  🌟 ¡BRUTAL! Bienvenido a la élite del Club de Fuerza Titán. 🌟")
            
            while True:
                try:
                    inv = int(input("\n  ▶ ¿Cuántos invitados deseas registrar en tu pase? (Máx 10): "))
                    if 0 <= inv <= 10:
                        self.invitados_principal = inv
                        if inv > 0:
                            print(f"  ✅ Excelente. Tus {inv} pases de invitado están activos.")
                        break
                    else:
                        print("  ⚠️ El límite máximo es de 10 invitados.")
                except ValueError:
                    print("  ⚠️ Por favor, ingresa un número válido.")
        else:
            print("\n  👍 Entendido. Tu pase se mantendrá como Estándar por los momentos.")
            
        print("\n        GUARDANDO PERFIL EN LA BASE DE DATOS...           ")
        self.guardar_registro(id_principal, self.nombre_socio_principal, self.edad_socio_principal, self.socio_principal_vip, self.clave_maestra, self.invitados_principal, fuerza_1rm_principal)
        
        print("\n        INICIANDO SISTEMA DE GESTIÓN...           ")

    def verificar_socio(self):
        print(f"\n[🔒 ACCESO RESTRINGIDO - Seguridad de {self.nombre_socio_principal}]")
        intento = input("▶ Ingresa tu clave de seguridad: ").strip()
        return intento == self.clave_maestra

    # ==========================================================================
    # 2. GESTIÓN DE DATOS (BASE DE DATOS)
    # ==========================================================================
    def guardar_registro(self, id_socio, nombre, edad, es_vip, clave, invitados, fuerza_1rm):
        if es_vip:
            tipo = f"VIP 👑 (+{invitados} inv)" if invitados > 0 else "VIP 👑"
        else:
            tipo = "Estándar"
            
        try:
            with open("registros_club.txt", "a", encoding="utf-8") as f:
                f.write(f"ID: #{id_socio} | Nombre: {nombre} | Edad: {edad} | Pase: {tipo} | 1RM: {fuerza_1rm:.2f} | Clave: {clave.strip()}\n")
            print("💾 [Registro guardado exitosamente]")
        except OSError: 
            print("⚠️ Error al guardar en la base de datos.")

    def ver_registros(self):
        if not self.verificar_socio(): return
        print("\n--- BASE DE DATOS DEL CLUB ---")
        try:
            with open("registros_club.txt", "r", encoding="utf-8") as f:
                contenido = f.read()
                print(contenido if contenido.strip() != "" else "La base de datos está vacía.")
        except FileNotFoundError: 
            print("⚠️ No se encontraron registros.")

    def buscar_cliente(self):
        print("\n--- BUSCADOR DE SOCIOS ---")
        id_buscado = input("▶ ID a buscar: ").strip()
        try:
            with open("registros_club.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    if f"ID: #{id_buscado}" in linea:
                        print(f"✅ {linea.strip()}")
                        return
                print("❌ ID no encontrado.")
        except FileNotFoundError: 
            print("⚠️ Base de datos vacía o no encontrada.")

    def eliminar_cliente(self):
        if not self.verificar_socio(): return
        print("\n--- DAR DE BAJA A UN CLIENTE ---")
        id_borrar = input("▶ ID a eliminar: ").strip()
        try:
            with open("registros_club.txt", "r", encoding="utf-8") as f:
                lineas = f.readlines()
            with open("registros_club.txt", "w", encoding="utf-8") as f:
                borrado = False
                for linea in lineas:
                    if f"ID: #{id_borrar}" not in linea: f.write(linea)
                    else: borrado = True
            print("✅ Cliente eliminado con éxito." if borrado else "❌ ID no encontrado.")
        except Exception: 
            print("⚠️ Error al procesar la solicitud.")

    # ==========================================================================
    # 3. HERRAMIENTAS Y REGISTRO DE NUEVOS CLIENTES
    # ==========================================================================
    def registrar_cliente(self):
        if not self.verificar_socio(): return
        print("\n--- Registrar Nuevo Socio ---")
        nombre = input("▶ Nombre del cliente: ").strip()
        try:
            edad = int(input("▶ Edad: "))
        except ValueError:
            print("⚠️ Error: La edad debe ser un número."); return
            
        if edad < 18:
            print("❌ Acceso denegado: Solo se permiten mayores de edad."); return
            
        print("\n--- EVALUACIÓN DE FUERZA INICIAL ---")
        print("Ingresa los datos para rankear al cliente en el Tablero de Titanes.")
        try:
            peso = float(input("▶ Peso máximo levant
