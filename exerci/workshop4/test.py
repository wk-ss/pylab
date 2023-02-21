# vamos importar a biblioteca NumPy
import numpy as np

# método principal

  # vamos criar uma matriz identidade de 4 linhas e 4 colunas


#matriz_identidade = np.twos(shape=(1,2,3))


#print("A matriz identidade gerada foi:\n{0}".format(matriz_identidade))
galera=[]
dado=[]
maior=[]
menor=[]
for i in range(2):
   dado.append(input("digite o seu nome: "))
   dado.append(int(input("sua idade: ")))
   galera.append(dado[:])
   dado.clear()
for p in galera:
    if p[1]>=21:
        print(f"{p[0]} é maior")
        maior.append(p[:])
    else:
        print(f"{p[0]} é de menor")
        menor.append(p[:])
print(galera)
print(maior)
print(menor)