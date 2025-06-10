miLista = [1,2,3,4,5]

for ele in miLista:
    print(ele)
print("Agergar")
print(miLista[2])
miLista.append(20)#agrega al final
miLista.insert(1, "pepe")#agrega donde le digamos

for ele in miLista:
    print(ele)
print("Eliminar")
try:
    miLista.remove("pepe")
except ValueError as ex:
    print("no se encuentra el dato a eliminar")
else:
    print("Elimino correctamente")
try:    
    miLista.remove(9)
except ValueError as ex:
    print("no se encuentra el dato a eliminar")
for ele in miLista:
    print(ele)

print("ordenar")
miLista.insert(1, 5)
for ele in miLista:
    print(ele)
miLista.sort()#ordena la lista

miLista.reverse()#dar vuelta la lista
for ele in miLista:
    print(ele)