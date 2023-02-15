def escrita():
    with open('teste.txt','w') as arq:
        nome=input('digite o seu nome: ')
        arq.write(nome+'\n')

def leitura():
    with open('teste.txt','r') as arquivo:
        print(arquivo.read())
        for linha in arquivo:
            print(linha[:-1])

escrita()
leitura()