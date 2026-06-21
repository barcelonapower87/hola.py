# 1. Definición de datos (¡Aquí van los inputs!)
# Pedimos el nombre y la edad al usuario antes de hacer cualquier lógica
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: ")) # El int() es necesario para que el programa entienda que es un número

# 2. Procesamiento (Tu lógica 'if-else' se mantiene igual)
if edad >= 18:
    print(f"¡Bienvenido {nombre}! Puedes pasar al club.")
    # ... (aquí va el resto de tu lógica para la zona VIP)
else:
    print(f"Lo siento {nombre}, eres menor.")
    # ... (aquí va tu lógica para los años restantes)



