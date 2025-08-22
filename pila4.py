# llenar pilaFia con los 15 primeros numeros consecutivos
#eliminas el tercero y septimo y lo imprimes nuevamente



pilafia = []
for i in range(1, 16):
    pilafia.append(i)

print("Pila original:", pilafia)

ter=2
sept=6

pilafia.pop(ter)
pilafia.pop(sept)

print("\pila despues de elimar",pilafia)




