s = int(input())
totala = 0
totalb = 0
totalc = 0
totaln = 0
totalbrancos= 0
maior = [0]*3

while (s !=0):
    a = int(input())
    b = int(input())
    c = int(input())
    brancos = int(input())
    nulos = int(input())

    totala = a + totala
    totalb = b + totalb
    totalc = c + totalc
    totalbrancos = brancos + totalbrancos
    totaln = nulos + totaln
    s = int(input())
total = totala+totalb+totalc+totalbrancos+totaln
#Mais votado
maior = [totala, totalb, totalc]
maior.sort(reverse=True)
maisvotado = maior[0]

if(maisvotado == 0 or (totala == totalb == totalc)):
    maisvotadostr = ''
elif (maisvotado == totala):
    maisvotadostr =  'A'
elif (maisvotado == totalb):
    maisvotadostr = 'B'
else:
    maisvotadostr = 'C'
if (totala+totalb+totalc>(totalbrancos+totaln)):
    valido = 'True'
else:
    valido = 'False'
if (maisvotado == 0):
    segundoturno = 'False'
elif (maisvotado>= round(((totala+totalb+totalc)/2)+0.5,0)):
    segundoturno = 'False'

else:
    segundoturno = 'True'

validos = totala+totalb+totalc

print('Numero de votantes: %i' %total)
print('Total A: %i' %totala)
print('Total B: %i' %totalb)
print('Total C: %i' %totalc)
print('Brancos: %i' %totalbrancos)
print('Nulos: %i' %totaln)
print('Validos: %i' %validos)
print('Candidato mais votado: %s' %maisvotadostr)
print('Eleicao valida? %s' %valido)
print('Segundo turno? %s' %segundoturno)