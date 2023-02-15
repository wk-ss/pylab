# Escreva um programa que receba como entrada a duração
# de cada uma das cinco músicas que ela já escolheu, e
# exiba qual o tempo total de entretenimento garantido.
minTOTAL=0
secTOTAL=0
for i in range(5):
    min=int(input())
    sec=int(input())
    minTOTAL+=min
    secTOTAL+=sec

h=0
m=(secTOTAL//60)+minTOTAL#m=divisiao inteira de (total de secundos/60)+(total de min)
s=secTOTAL%60#s=resto da divisao de (total de secundos/60)
if m>60:
    h=m//60
    m=h%60
    s=m%60


print(h)
print(m)
print(s)