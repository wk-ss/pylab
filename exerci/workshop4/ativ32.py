'''Leia um inteiro N.Depois, leia até 20 inteiros X0, X1, ..., X20.
Seu programa deve imprimir quantas vezes o inteiro N aparece nos X inteiros.'''
lista=[]
i=0
cont=0
n=x=int(input())
while i<20:
    x=int(input())
    if x==-1:
        break
    lista.append(x)
    i+=1
for num in lista:
    if num==n:
        cont+=1
print(f'{n} aparece {cont} vezes')