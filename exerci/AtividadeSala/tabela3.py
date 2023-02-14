tab={}
n=idMax = idMin = qtd =0
cpf =int(input("cpf: "))
while cpf>0:
    cpf = int(input("digite o cpf :"))
    nome=input("nome:")
    idade=int(input("idade"))
    tab[cpf]=(nome,idade)
    qtd+=1
    cpf=int(input("cpf:"))
if cpf>0:
    print("leitura interrrompida,ultimo cpf desprezado")
n=int(input("invalidoo: "))
for i in range (n):
    idMin=int(input("idade minima:"))
    while idMin<0:
        idMin=int(input("invalidade :idade minima:"))
    idMax=int(input("idade minima:"))
    qtd2=0
    for ch in tab:
        if tab[ch][1]>= idMin and tab[ch][1]<=idMax:
            print(ch,tab[ch][0],tab[ch][1])
            qtd2+=1
        print("qtd de a ")
        