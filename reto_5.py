
A = []
B = []
C = []
D = []

#Parte1

listatres = ['verde', 'verde', 'amarillo', 'rojo', 'verde', 'amarillo', 'rojo', 'amarillo', 'rojo', 'verde']

for i in range(len(listatres)):
    if listatres[i] not in C:
      C.append(listatres[i])
print(C)  


#parte2

etiquetas = ['verde', 'verde', 'amarillo', 'rojo', 'verde', 'amarillo', 'rojo', 'amarillo', 'rojo', 'verde']
elementos = [0, 2, 4, 8]
etiqueta = ['rojo']

#print(etiquetas[2])

for it in elementos:
  if etiqueta[0] == etiquetas[it]:
     D.append(it)

print(D)


listauno = [3,5,7,10,15,16]
listados = [4,10,5,8]
#Parte3

for it in listauno:
  if it not in listados:
    B.append(it)

# 4 parte
for it in listauno:
  if it in listados:
    A.append(it)

print(B)
print(len(A))