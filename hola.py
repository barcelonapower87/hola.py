import random

class SistemaClub:
    def __init__(self):
        # Aquí inicializamos el estado del sistema dentro del objeto
        self.clave_maestra = ""
        self.nombre_socio_principal = ""

    # ==========================================================================
    # 1. SEGURIDAD Y CONFIGURACIÓN
    # ==========================================================================
    def configuracion_inicial(self):
        print("\n==================================================")
        print("  BIENVENIDO - CREAR CUENTA DE SOCIO PRINCIPAL    ")
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
                print("  ✅ Clave configurada.")
                break
        print("\n        INICIANDO SISTEMA DE GESTIÓN...           ")

    def verificar_socio(self):
        print(f"\n[🔒 ACCESO RESTRINGIDO - Seguridad de {self.nombre_socio_principal}]")
        intento = input("▶ Ingresa tu clave de seguridad: ").strip()
        return intento == self.clave_maestra

    # ==========================================================================
    # 2. GESTIÓN DE DATOS (BASE DE DATOS)
    # ==========================================================================
    def guardar_registro(self, id_socio, nombre, edad, es_vip, clave):
        tipo = "VIP" if es_vip else "Estándar"
        try:
            with open("hola.txt", "a", encoding="utf-8") as f:
                f.write(f"ID: #{id_socio} | Nombre: {nombre} | Edad: {edad} | Pase: {tipo} | Clave: {clave}\n")
            print("💾 [Registro guardado]")
        except: print("⚠️ Error al guardar.")

    def ver_registros(self):
        if not self.verificar_socio(): return
        print("\n--- BASE DE DATOS ---")
        try:
            with open("hola.txt", "r", encoding="utf-8") as f:
                print(f.read() if f.read() != "" else "La base de datos está vacía.")
        except: print("⚠️ No hay registros.")

    def buscar_cliente(self):
        print("\n--- BUSCADOR ---")
        id_buscado = input("▶ ID a buscar: ").strip()
        try:
            with open("hola.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    if f"ID: #{id_buscado}" in linea:
                        print(f"✅ {linea.strip()}")
                        return
                print("❌ ID no encontrado.")
        except: print("⚠️ Base de datos vacía.")

    def eliminar_cliente(self):
        if not self.verificar_socio(): return
        id_borrar = input("▶ ID a eliminar: ").strip()
        try:
            with open("hola.txt", "r", encoding="utf-8") as f:
                lineas = f.readlines()
            with open("hola.txt", "w", encoding="utf-8") as f:
                borrado = False
                for linea in lineas:
                    if f"ID: #{id_borrar}" not in linea: f.write(linea)
                    else: borrado = True
            print("✅ Cliente eliminado." if borrado else "❌ ID no encontrado.")
        except: print("⚠️ Error.")

    # ==========================================================================
    # 3. HERRAMIENTAS Y REGISTRO
    # ==========================================================================
    def registrar_cliente(self):
        if not self.verificar_socio(): return
        nombre = input("▶ Nombre del cliente: ").strip()
        edad = int(input("▶ Edad: "))
        if edad < 18:
            print("❌ Acceso denegado: Menor de edad."); return
        es_vip = input("▶ ¿VIP? (s/n): ").lower() == 's'
        id_socio = random.randint(10000, 99999)
        clave = input("▶ Crea clave para el cliente: ").strip()
        self.guardar_registro(id_socio, nombre, edad, es_vip, clave)
        print(f"✅ Registro exitoso. ID asignado: #{id_socio}")

    def calculadora_1rm(self):
        print("\n--- CALCULADORA 1RM ---")
        try:
            p = float(input("▶ Peso: "))
            r = int(input("▶ Reps: "))
            print(f"💪 Tu 1RM estimado: {p * (1 + (0.0333 * r)):.2f}")
        except: print("⚠️ Error: Solo números.")

    # ==========================================================================
    # 4. MENÚ PRINCIPAL
    # ==========================================================================
    def menu(self):
        while True:
            print("\n==================================================")
            print("    SISTEMA DE ACCESO - CLUB DE FUERZA TITÁN      ")
            print("==================================================")
            print("  [1] Registrar nuevo cliente")
            print("  [2] Calculadora 1RM")
            print("  [3] Buscar cliente")
            print("  [4] Ver registros")
            print("  [5] Eliminar cliente")
            print("  [6] Salir del sistema")
            
            opcion = input("▶ Opción: ").strip()
            if opcion == '1': self.registrar_cliente()
            elif opcion == '2': self.calculadora_1rm()
            elif opcion == '3': self.buscar_cliente()
            elif opcion == '4': self.ver_registros()
            elif opcion == '5': self.eliminar_cliente()
            elif opcion == '6': break
            else: print("⚠️ Opción inválida.")

# ==============================================================================
# ARRANQUE
# ==============================================================================
def iniciar():
    club = SistemaClub()
    while True:
        print("\n==================================================")
        print("             CLUB DE FUERZA TITÁN                 ")
        print("                 ==== 💪 ====                     ")
        print("==================================================")
        print("  [1] Crear cuenta de socio principal")
        print("  [2] Salir")
        opcion = input("▶ Opción: ").strip()
        
        if opcion == '1':
            club.configuracion_inicial()
            club.menu()
            break
        elif opcion == '2':
            break
        else: print("⚠️ Opción inválida.")

if __name__ == "__main__":
    iniciar()
