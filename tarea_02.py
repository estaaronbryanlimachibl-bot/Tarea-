# Máquina expendedora

saldo = float(input("Ingrese su saldo en Bs.: "))
cantidad_productos = 0

while True:
    print("\n--- MÁQUINA EXPENDEDORA ---")
    print("1. Galletas - 5 Bs.")
    print("2. Refresco - 8 Bs.")
    print("3. Chocolate - 10 Bs.")
    print("4. Papas fritas - 12 Bs.")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        precio = 5
    elif opcion == 2:
        precio = 8
    elif opcion == 3:
        precio = 10
    elif opcion == 4:
        precio = 12
    elif opcion == 5:
        break
    else:
        print("Opción no válida.")
        continue

    if saldo >= precio:
        saldo -= precio
        cantidad_productos += 1
        print("Compra realizada con éxito.")
        print("Saldo restante:", saldo, "Bs.")
    else:
        print("Saldo insuficiente para comprar este producto.")

print("\n--- Total ---")
print("Cantidad de productos comprados:", cantidad_productos)
print("Saldo final:", saldo, "Bs.")