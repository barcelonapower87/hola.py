# 1. Definición de variables (Valores de prueba con Juan)
nombre = "Juan"
edad = 18

# 2. Preparación de datos (Validación y cálculo base)
limite_edad = 18
faltan = limite_edad - edad

# 3. Procesamiento (Lógica de decisión con condiciones)
if edad >= limite_edad:
    resultado = "¡Bienvenido " + nombre + "! Puedes pasar al club."
    vip = True
else:
    # Lógica inteligente para definir el plural o singular de los años
    años_str = "año" if faltan == 1 else "años"
    resultado = "Lo siento " + nombre + ", eres menor. Vuelve en " + str(faltan) + " " + años_str + "."
    vip = False

# 4. Salida (Presentación de resultados en pantalla)
print("------------------------------")
print("PROBANDO CON: " + nombre + " (" + str(edad) + " años)")
print("------------------------------")
print(resultado)

if vip:
    print("Disfruta de la zona VIP.")
print("------------------------------")


