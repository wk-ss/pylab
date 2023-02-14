# Crie uma lista contendo todos os números primos entre 1 e 100.
# Em seguida, faça outra lista com a média entre os pares consecutivos, dois a dois, 
# sem levar em consideração o primeiro elemento.
# Finalize com uma matriz quadrada com os elementos das posições 1 a 9 da segunda lista. 

#lista 1 numeors primos

lista1=[]
for c in range(1,100):
    VetorPrimos = []
    for loop in range(1,c+1):
        if c % loop == 0:
            VetorPrimos.append(loop)
    if len(VetorPrimos)==2:
        lista1.append(c)
print(lista1)
print(len(lista1))


del lista1[0]
#lista2 soma e media dos elementos do a parti do segundo elemento
lista2=[]
for c in range(0,len(lista1),2):
        m = (lista1[c]+lista1[c+1])/2
        lista2.append(m)
print(lista2)
matri=[]
for i in range (0,3):
    matri.append([0]*3)
cont=0
for c in range(3):
   for i in range(3):
        cont+=1
        matri[c][i]=lista2[cont]

for c in range(3):
    print(matri[c])
