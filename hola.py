import random

class SistemaClub:
    def __init__(self):
        self.clave_maestra = ""
        self.nombre_socio_principal = ""
        self.socio_principal_vip = False

    # ==========================================================================
    # 1. SEGURIDAD Y CONFIGURACIÓN (CON GRAN OFERTA VIP INICIAL)
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

        # 🌟 GRAN OFERTA PUBLICITARIA VIP (JUSTO DESPUÉS DE CREAR LA CUENTA)
        print("\n==================================================")
        print(" 🔥 ¡ESPERA! TENEMOS UNA OFERTA EXCLUSIVA PARA TI 🔥")
        print("==================================================")
        print(f"  Hola, {self.nombre_socio_principal}. Tu cuenta estándar ya está activa,")
        print("  pero... ¿por qué conformarte con lo ordinario?")
        print("\n  👑 ¡MEJORA TU MEMBRESÍA AL PASE VIP TITÁN! 👑")
        print("  ------------------------------------------------")
        print("  🚪 ACCESO EXCLUSIVO A LA SALA PRIVADA VIP")
        print("     Un espacio reservado solo para atletas de élite.")
        print("     Evita las aglomeraciones y entrena a tu propio ritmo.")
        print("\n  🤖 MÁQUINAS CON TECNOLOGÍA DE ÚLTIMA GENERACIÓN")
        print("     Acceso a equipamiento inteligente que analiza tu fuerza,")
        print("     ajusta la resistencia neumática por pantalla táctil")
        print("     y optimiza automáticamente cada una de tus repeticiones.")
        print("==================================================")
        
        oferta = input("▶ ¿Deseas ascender a Miembro VIP ahora mismo? (s/n): ").strip().lower()
        if oferta == 's':
            self.socio_principal_vip = True
            print("\n  🌟 ¡BRUTAL! Bienvenido a la élite del Club de Fuerza Titán. 🌟")
            print("  Tu pase ha sido actualizado. Disfruta de la Sala Tecnológica Privada.")
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
    def guardar_registro(self, id_socio, nombre, edad, es_vip, clave):
        tipo = "VIP 👑" if es_vip else "Estándar"
        try:
            with open("registros_club.txt", "a", encoding="utf-8") as f:
                f.write(f"ID: #{id_socio} | Nombre: {nombre} | Edad: {edad} | Pase: {tipo} | Clave: {clave}\n")
            print("💾 [Registro guardado exitosamente]")
        except: print("⚠️ Error al guardar en la base de datos.")

    def ver_registros(self):
        if not self.verificar_socio(): return
        print("\n--- BASE DE DATOS DEL CLUB ---")
        try:
            with open("registros_club.txt", "r", encoding="utf-8") as f:
                contenido = f.read()
                print(contenido if contenido.strip() != "" else "La base de datos está vacía.")
        except: print("⚠️ No se encontraron registros.")

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
        except: print("⚠️ Base de datos vacía o no encontrada.")

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
        except: print("⚠️ Error al procesar la solicitud.")

    # ==========================================================================
    # 3. HERRAMIENTAS Y REGISTRO DE NUEVOS CLIENTES
    # ==========================================================================
    def registrar_cliente(self):
        if not self.verificar_socio(): return
        print("\n--- Registrar Nuevo Socio ---")
        nombre = input("▶ Nombre del cliente: ").strip()
        try:
            edad = int(input("▶ Edad: "))
        except:
            print("⚠️ Error: La edad debe ser un número."); return
            
        if edad < 18:
            print("❌ Acceso denegado: Solo se permiten mayores de edad."); return
        
        print("\n--- OFRECER UPGRADE VIP ---")
        print("👉 Recuerda ofrecer el acceso a la Sala Privada con máquinas tecnológicas.")
        respuesta_vip = input("▶ ¿El cliente adquiere el Pase VIP? (s/n): ").lower()
        es_vip = (respuesta_vip == 's')
        
        id_socio = random.randint(10000, 99999)
        clave = input("▶ Asigna una clave para el cliente: ").strip()
        
        self.guardar_registro(id_socio, nombre, edad, es_vip, clave)
        print(f"✅ ¡Registro completado! ID asignado: #{id_socio}")

    def calculadora_1rm(self):
        print("\n--- CALCULADORA DE FUERZA (1RM) ---")
        try:
            p = float(input("▶ Peso levantado (kg/lbs): "))
            r = int(input("▶ Repeticiones logradas: "))
            if r <= 0 or p <= 0: print("⚠️ Los valores deben ser mayores a cero."); return
            print(f"💪 Tu repetición máxima teórica es: {p * (1 + (0.0333 * r)):.2f}")
        except: print("⚠️ Error: Ingresa únicamente números válidos.")

    # ==========================================================================
    # 4. MENÚ PRINCIPAL DEL SISTEMA
    # ==========================================================================
    def menu(self):
        while True:
            rango = "VIP 👑" if self.socio_principal_vip else "Estándar"
            print("\n==================================================")
            print("    SISTEMA DE ACCESO - CLUB DE FUERZA TITÁN      ")
            print(f"    Socio Principal: {self.nombre_socio_principal} [{rango}]")
            print("==================================================")
            print("  [1] Registrar nuevo cliente")
            print("  [2] Calculadora de fuerza (1RM)")
            print("  [3] Buscar cliente")
            print("  [4] Ver todos los registros")
            print("  [5] Eliminar cliente")
            print("  [6] Salir del Menú")
            
            opcion = input("▶ Elige una opción: ").strip()
            if opcion == '1': self.registrar_cliente()
            elif opcion == '2': self.calculadora_1rm()
            elif opcion == '3': self.buscar_cliente()
            elif opcion == '4': self.ver_registros()
            elif opcion == '5': self.eliminar_cliente()
            elif opcion == '6': 
                print("🔒 Cerrando sesión de administración...")
                break
            else: print("⚠️ Opción inválida.")

# ==============================================================================
# ARRANQUE OBLIGATORIO DEL PROGRAMA
# ==============================================================================
def iniciar():
    club = SistemaClub()
    while True:
        print("\n==================================================")
        print("             CLUB DE FUERZA TITÁN                 ")
        print("                   == 💪 ==                       ")
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
