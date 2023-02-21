numeros = []
terminou = False
while not terminou:
    entrada = int(input())
    if entrada == -1:
            terminou = True
    else:
        numeros.append(entrada)
soma=0
for p in numeros:
    soma+=p
media=soma/len(numeros)
print(f'{media:.2f}')