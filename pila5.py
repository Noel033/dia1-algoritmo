#una pila para 20 nombres imprimes aplicando el concepto de LIFO
#pero sacas uno pero sacadno LIFO

#ahora tiene que morir al primero

pilaFia = []

# Ingresar 3 nombres (puedes cambiar a 20 si quieres)
for i in range(3):
    nom = input("Ingrese su nombre: ")
    pilaFia.append(nom)

# Mostrar pila original
print("\nPila original:")
print(pilaFia)

# Eliminar el último elemento (LIFO)
elimUltim = pilaFia.pop()
print("\nElemento eliminado (LIFO):", elimUltim)

# Mostrar pila después de eliminar el último
print("\nPila después de eliminar el último:")
for i in range(len(pilaFia) - 1, -1, -1):
    print(pilaFia[i])

# Eliminar el primero (no LIFO, pero manualmente)
elimPrim = pilaFia.pop(0)
print("\nElemento eliminado (el primero ingresado):", elimPrim)

# Mostrar pila final
print("\nPila final:")
for i in range(len(pilaFia) - 1, -1, -1):
    print(pilaFia[i])

