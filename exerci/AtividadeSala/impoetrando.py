import random
lista=[]
def numeros_loterias(qtd,min,max):
    for c in range(qtd):
        numeros=random.randrange(min,max)
        while numeros in lista:
            numeros=random.randrange(min,max)
        lista.append(numeros)

qtd,min,max=(map(int,input("DIGITE A QUANTIDADE DE NUMEROS RAMDON ,MINIMO ,MAXIMO:").split()))
while qtd>(max-min) or qtd<0:
    qtd,min,max=(map(int,input("quantidade menor q o range de 2 numeros").split()))

numeros_loterias(qtd,min,max)
print(lista)