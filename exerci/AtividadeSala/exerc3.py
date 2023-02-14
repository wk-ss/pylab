aluno=[]
cont=0
quantidade=int(input('digite a quandidade de alunos: '))
for loop in range(quantidade):
    aluno.append(str(input('digite o nome dos alunos: ')))
    cont+=1
for liip in range(quantidade):
    print (f"{aluno[liip]},{liip+1}")

nome=input('digite o nome do aluno na busca: ')
for laap in range(quantidade):
    if nome==aluno[laap]:
        print(f'nome encontrado na possiçao {laap+1}')
