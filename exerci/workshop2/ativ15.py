import math
def calcular_prestacao(financiamento, quantidadePrestacao, taxa):
    ant = ((1 + taxa)*quantidadePrestacao - 1)/(taxa((1 + taxa)**quantidadePrestacao))
    parcelamento = financiamento/ant
    return parcelamento

financiamento = float(input())
quantidadePrestacao = int(input())
taxa = float(input())

retorno = calcular_prestacao(financiamento, quantidadePrestacao, taxa)

print(math.trunc(retorno))