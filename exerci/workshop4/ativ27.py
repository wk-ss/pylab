alu=int(input())
notas=[]
proximo=[]

somat=0
def media(somat,alu):
    return somat/alu
for i in range (alu):
    aluno=(float(input()))
    notas.append(aluno)
    somat+=aluno
notas.sort(reverse=False)
m=media(somat,alu)

for prox in notas:
    proxim=prox-m
    if proxim<0:
        proxim=proxim*-1
        proximo.append(proxim)
    else:
        proximo.append(proxim)

id = proximo.index(min(proximo))
p= notas[id]

d=p-m
p=d+m
if d<0:
    d=d*-1

print(f'MEDIA: {m:.2f}')
print(f'MAIS PROXIMO: {p:.2f}')
print(f'DIFERENCA: {d:.2f}')
