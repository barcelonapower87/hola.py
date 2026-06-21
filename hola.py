def sistema_registro_comercial():
    print("==================================================")
    print("    SISTEMA DE ACCESO - CLUB DE FUERZA TITÁN      ")
    print("==================================================")
    print("Bienvenido. Sigue los pasos para tu registro.\n")
    
    programa_abierto = True
    
    while programa_abierto:
        print("--- Nuevo Cliente ---")
        
        # 1. EXPLICACIÓN Y PREGUNTA DEL NOMBRE
        print("\n[?] Necesitamos tu nombre para personalizar tu pase de acceso físico.")
        nombre = input("▶ Por favor, ingresa tu nombre: ").strip()
        
        while not nombre:
            print("  ⚠️ Error: El nombre no puede estar vacío.")
            nombre = input("▶ Ingresa tu nombre nuevamente: ").strip()
            
        # 2. EXPLICACIÓN Y PREGUNTA DE LA EDAD
        print("\n[?] Solicitamos tu edad por motivos de seguridad. Nuestras instalaciones exigen un mínimo de 18 años.")
        edad = -1
        while edad < 0:
            try:
                edad = int(input("▶ Por favor, ingresa tu edad en números (ej. 20): ").strip())
                
                if edad < 0 or edad > 120:
                    print("  ⚠️ Error: Ingresa una edad válida.")
                    edad = -1 
            except ValueError:
                print("  ⚠️ Error: Has ingresado texto. Usa solo números enteros.")

        # 3. EVALUACIÓN Y OFERTA VIP (LA NUEVA LÓGICA)
        print("\n--------------------------------------------------")
        if edad >= 18:
            # Si pasó la prueba de edad, le ofrecemos el VIP
            print(f"✅ Requisitos cumplidos, {nombre}.")
            print("\n[?] OFERTA OPCIONAL: Pase VIP por $50 adicionales.")
            print("    Beneficios: Sin fila de espera, acceso a la zona de spa, y batidos de cortesía.")
            
            es_vip = False
            while True:
                respuesta_vip = input("▶ ¿Deseas adquirir la entrada VIP? (s/n): ").strip().lower()
                
                if respuesta_vip in ['s', 'si', 'sí']:
                    es_vip = True
                    break
                elif respuesta_vip in ['n', 'no']:
                    break # es_vip ya es False por defecto
                else:
                    print("  ⚠️ Por favor, responde solo con 's' (Sí) o 'n' (No).")
            
            # Mensaje final personalizado según su compra
            print("\n--------------------------------------------------")
            if es_vip:
                print(f"🌟 ¡Bienvenido a la experiencia VIP, {nombre}!")
                print("   Tu pase premium ha sido generado. Pasa directo a la zona exclusiva.")
            else:
                print(f"✅ ¡Registro estándar exitoso! Bienvenido, {nombre}.")
                print("   Tu pase básico ha sido generado. Disfruta tu entrenamiento.")
                
        else:
            # Si no pasó la prueba de edad, lo rechazamos directamente
            print(f"❌ Acceso denegado. Lo sentimos, {nombre}.")
            print(f"   Actualmente tienes {edad} años. Por políticas del club,")
            print("   no podemos permitirte el acceso a las instalaciones aún.")
        print("--------------------------------------------------")
        
        # 4. BUCLE PARA REGISTRAR A MÁS PERSONAS
        while True:
            respuesta = input("\n¿Deseas registrar a otra persona? (s/n): ").strip().lower()
            if respuesta in ['s', 'si', 'sí']:
                print("\n" + "="*50)
                break 
            elif respuesta in ['n', 'no']:
                programa_abierto = False 
                break 
            else:
                print("  ⚠️ Por favor, responde solo con 's' (Sí) o 'n' (No).")

    print("\n==================================================")
    print("   SISTEMA CERRADO. ¡Corte de caja finalizado! ")
    print("==================================================")

if __name__ == "__main__":
    sistema_registro_comercial()



