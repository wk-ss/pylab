# Escreva a funcao media_pares_impares(lista) abaixo:
def media_pares_impares(lista):
    listainp=[]
    listapar=[]
    somaimp=0
    somapar=0

    for p in lista:
        if p %2==0:
            listapar.append(p)
            somapar+=p
        else:
            listainp.append(p)
            somaimp+=p

    mediapar=somapar/len(listapar)
    mediaimp=somaimp/len(listainp)
    return print(f'{mediapar}\n{mediaimp}')

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
lista = eval(input())
media_pares_impares(lista)