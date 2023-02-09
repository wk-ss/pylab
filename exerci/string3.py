texto=input("tetxo normal:")
proc=input("digite um texto a ser procurado:")

cont=0
pos=texto.find(proc)
while pos !=-1:
    cont+=1
    pos=texto.find(proc,pos+1)
print(cont)#a quantidade de cada letra
print(texto.count(proc))#a quantidadde de cada palavra for repedido