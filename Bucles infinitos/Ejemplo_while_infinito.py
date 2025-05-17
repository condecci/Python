# Almacena el actual número más grande aquí.
Numero_mas_grande= -999999999

# Ingresa el primer valor.
numero_usuario = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while numero_usuario != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if numero_usuario > Numero_mas_grande:
        # Sí si, se actualiza largest_number.
        Numero_mas_grande = numero_usuario
    # Ingresa el siguiente número.
    numero_usuario = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", Numero_mas_grande)

