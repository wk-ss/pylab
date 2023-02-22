"""Escreva a função todos_os_indices(seq, x) que recebe uma sequência seq (lista, tupla ou string)
, e devolve uma lista em Python com todos os índices de seq em que o valor x ocorre.
Caso não exista nenhuma ocorrência de x, a função devolve uma lista vazia."""

lista=[]
def todos_os_indices(sequencia, valor):
    for p in range(len(sequencia)):
        if sequencia[p]==valor:
            lista.append(p)

    return (lista)

sequencia = eval(input())
valor = eval(input())
resultado = todos_os_indices(sequencia, valor)
if isinstance(resultado, list):
	if len(resultado) > 0:
		for item in resultado:
			print(item)
	else:
		print('lista vazia')
else:
	print('Erro. Voce deve devolver uma lista')