"""O seu programa vai ler os dados da entrada e guarda-los,
em ordem crescente, em uma lista x. Imprima o quinto elemento da lista.
O código abaixo já faz a leitura dos dados e a ordenação da lista.
Você só precisa complementar o código para que ele imprima o quinto elemento da lista"""
x = input().split(',')
x.sort()
print(x[4])