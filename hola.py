import random

class SistemaClub:
    def __init__(self):
        self.clave_maestra = ""
        self.nombre_socio_principal = ""
        self.socio_principal_vip = False
        self.invitados_principal = 0

    # ==========================================================================
    # 1. SEGURIDAD Y CONFIGURACIÓN
    # ==========================================================================
    def configuracion_inicial(self):
        print("\n==================================================")
        print("  BIENVENIDO - CONFIGURAR SOCIO PRINCIPAL        ")
        print("==================================================")
        
        while True:
            nombre = input("▶ Ingresa tu nombre: ").strip()
            if nombre != "" and nombre.replace(" ", "").isalpha():
                self.nombre_socio_principal = nombre
                break
            else:
                print("  ⚠️ Error: Ingresa un nombre válido (solo letras).")
                
        id_principal = random.randint(10000, 99999)
        print(f"\n✅ ¡Cuenta creada! Tu Etiqueta de socio Titán es: #{id_principal}")
        
        while True:
            self.clave_maestra = input(f"\n[?] {self.nombre_socio_principal}, crea tu clave de seguridad: ").strip()
            if self.clave_maestra != "":
                print("  ✅ Clave de seguridad configurada con éxito.")
                break

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
        print("     Como VIP, podrás traer hasta 2 acompañantes contigo, ¡GRATIS!")
        print("==================================================")
        
        oferta = input("▶ ¿Deseas ascender a Miembro VIP ahora mismo? (s/n): ").strip().lower()
        if oferta == 's':
            self.socio_principal_vip = True
            print("\n  🌟 ¡BRUTAL! Bienvenido a la élite del Club de Fuerza Titán. 🌟")
            
            while True:
                try:
                    inv = int(input("\n  ▶ ¿Cuántos invitados deseas registrar en tu pase? (0, 1 o 2): "))
                    if 0 <= inv <= 2:
                        self.invitados_principal = inv
                        if inv > 0:
                            print(f"  ✅ Excelente. Tus {inv} pases de invitado están activos.")
                        break
                    else:
                        print("  ⚠️ El límite máximo es de 2 invitados.")
                except ValueError:
                    print("  ⚠️ Por favor, ingresa un número válido.")
        else:
            print("\n  👍 Entendido. Tu pase se mantendrá como Estándar por los momentos.")
            
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
                # AÑADIMOS EL 1RM A LA BASE DE DATOS
                f.write(f"ID: #{id_socio} | Nombre: {nombre} | Edad: {edad} | Pase: {tipo} | 1RM: {fuerza_1rm:.2f} | Clave: {clave}\n")
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
    # 3. HERRAMIENTAS Y REGISTRO
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
            
        # NUEVO: EVALUACIÓN DE FUERZA PARA EL TABLERO
        print("\n--- EVALUACIÓN DE FUERZA INICIAL ---")
        print("Ingresa los datos para rankear al cliente en el Tablero de Titanes.")
        try:
            peso = float(input("▶ Peso máximo levantado (kg/lbs): "))
            reps = int(input("▶ Repeticiones logradas con ese peso: "))
            fuerza_1rm = peso * (1 + (0.0333 * reps)) if peso > 0 and reps > 0 else 0.0
            print(f"💪 1RM Inicial registrado: {fuerza_1rm:.2f}")
        except ValueError:
            print("⚠️ Datos inválidos. Se registrará 0.00 de fuerza base.")
            fuerza_1rm = 0.0
        
        print("\n--- OFRECER UPGRADE VIP ---")
        print("¡Hazte VIP y accede a nuestra SALA PRIVADA!")
        print("Incluye máquinas tecnológicas y la opción de traer hasta 2 invitados.")
        respuesta_vip = input("▶ ¿El cliente adquiere el Pase VIP por $50? (s/n): ").lower()
        es_vip = (respuesta_vip == 's')
        
        invitados = 0
        if es_vip:
            while True:
                try:
                    inv = int(input("▶ ¿Cuántos invitados desea registrar el cliente? (0, 1 o 2): "))
                    if 0 <= inv <= 2:
                        invitados = inv
                        break
                    else:
                        print("⚠️ El límite máximo es de 2 invitados.")
                except ValueError:
                    print("⚠️ Ingresa un número válido.")
        
        id_socio = random.randint(10000, 99999)
        clave = input("▶ Asigna una clave para el cliente: ").strip()
        
        self.guardar_registro(id_socio, nombre, edad, es_vip, clave, invitados, fuerza_1rm)
        
        if es_vip:
            print(f"\n🌟 ¡BIENVENIDO A LA ELITE VIP, {nombre.upper()}!")
            print("   Acceso autorizado a la Sala Privada tecnológica.")
        else:
            print(f"\n✅ Registro completado! ID asignado: #{id_socio}")

    def calculadora_1rm(self):
        print("\n--- CALCULADORA DE FUERZA (1RM) ---")
        try:
            p = float(input("▶ Peso levantado (kg/lbs): "))
            r = int(input("▶ Repeticiones logradas: "))
            if r <= 0 or p <= 0: print("⚠️ Los valores deben ser mayores a cero."); return
            print(f"💪 Tu repetición máxima teórica es: {p * (1 + (0.0333 * r)):.2f}")
        except ValueError: 
            print("⚠️ Error: Ingresa únicamente números válidos.")

    # ==========================================================================
    # 4. TABLERO DE TITANES (LEADERBOARD)
    # ==========================================================================
    def tablero_titanes(self):
        print("\n==================================================")
        print("          🏆 TABLERO DE TITANES (RANKING) 🏆      ")
        print("==================================================")
        try:
            with open("registros_club.txt", "r", encoding="utf-8") as f:
                lineas = f.readlines()
            
            atletas = []
            for linea in lineas:
                partes = linea.split('|')
                if len(partes) >= 6: # Asegura que la línea tiene todos los datos incluyendo el 1RM
                    nombre = partes[1].replace("Nombre:", "").strip()
                    pase = partes[3].replace("Pase:", "").strip()
                    try:
                        # Extraer el valor numérico del 1RM
                        rm_val = float(partes[4].replace("1RM:", "").strip())
                        atletas.append((nombre, pase, rm_val))
                    except ValueError:
                        pass
            
            if not atletas:
                print("  No hay atletas registrados con evaluación de fuerza aún.")
                return
                
            # Ordenar la lista de atletas de mayor a menor 1RM
            atletas.sort(key=lambda x: x[2], reverse=True)
            
            print(" RANK | NOMBRE           | FUERZA (1RM) | TIPO DE PASE")
            print("------------------------------------------------------")
            for i, atleta in enumerate(atletas[:10], 1): # Muestra el Top 10
                nombre, pase, rm = atleta
                print(f"  #{i:<2} | {nombre:<16} | {rm:<12.2f} | {pase}")
                
        except FileNotFoundError:
            print("⚠️ La base de datos está vacía. Registra a los primeros atletas.")

    # ==========================================================================
    # 5. MENÚ PRINCIPAL DEL SISTEMA
    # ==========================================================================
    def menu(self):
        while True:
            extra = f" (+{self.invitados_principal} Inv)" if self.invitados_principal > 0 else ""
            rango = f"VIP 👑{extra}" if self.socio_principal_vip else "Estándar"
            
            print("\n==================================================")
            print("    SISTEMA DE ACCESO - CLUB DE FUERZA TITÁN      ")
            print(f"    Socio Principal: {self.nombre_socio_principal} [{rango}]")
            print("==================================================")
            print("  [1] Registrar nuevo cliente")
            print("  [2] Calculadora libre de fuerza (1RM)")
            print("  [3] Buscar cliente")
            print("  [4] Ver todos los registros")
            print("  [5] Eliminar cliente")
            print("  [6] Salir del Menú")
            print("  [7] 🏆 Ver Tablero de Titanes (Ranking)")
            
            opcion = input("▶ Elige una opción: ").strip()
            if opcion == '1': self.registrar_cliente()
            elif opcion == '2': self.calculadora_1rm()
            elif opcion == '3': self.buscar_cliente()
            elif opcion == '4': self.ver_registros()
            elif opcion == '5': self.eliminar_cliente()
            elif opcion == '6': 
                print("🔒 Cerrando sesión de administración...")
                break
            elif opcion == '7': self.tablero_titanes()
            else: print("⚠️ Opción inválida.")

# ==============================================================================
# ARRANQUE OBLIGATORIO DEL PROGRAMA
# ==============================================================================
def iniciar():
    club = SistemaClub()
    while True:
        print("\n==================================================")
        print("             CLUB DE FUERZA TITÁN                 ")
        print("==================================================")
        print("                 ======                           ")
        print("               ==========                         ")
        print("              ====    ====                        ")
        print("    =======  ====  ==  ====                       ")
        print("   =========================                      ")
        print("    =======================                       ")
        print("      ===================                         ")
        print("        ===============                           ")
        print("           =========                              ")
        print("==================================================")
        print("  [1] Crear cuenta de socio")
        print("  [2] Salir")
        print("==================================================")
        opcion = input("▶ Opción: ").strip()
        
        if opcion == '1':
            club.configuracion_inicial()
            club.menu()
            break
        elif opcion == '2': 
            print("👋 ¡Nos vemos en los entrenamientos! Mantente fuerte.")
            break
        else: 
            print("⚠️ Opción inválida. Elige 1 o 2.")

if __name__ == "__main__":
    iniciar()
