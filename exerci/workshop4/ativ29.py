"""Escreva um programa onde os usuários podem digitar vários números inteiros,
um de cada vez. Quando quiser encerrar o programa, basta digitar -1.
Nessa hora o programa deverá exibir na tela a média aritmética dos números
digitados, com 2 casas decimais.
"""
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