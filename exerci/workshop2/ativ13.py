# Escreva um programa que receba como entrada a duração
# de cada uma das cinco músicas que ela já escolheu, e
# exiba qual o tempo total de entretenimento garantido.
musicamt=0
musicast=0
for i in range(5):
    musicam=int(input())
    musicas=int(input())
    musicamt+=musicam
    musicast+=musicas

h=0
ms=(musicast//60)+musicamt
s=musicast%60
if ms>60:
    h=ms//60
    ms=h%60
    s=ms%60


print(h)
print(ms)
print(s)