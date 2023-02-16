
valores=[]
with open('valores.csv','r') as arq_leitura:
    with open('valores.txt','w') as arq_escrita:
        for linha in arq_leitura:
                soma=sum(int(e) for e in linha.split(','))
                
                for num in linha.strip().split(','):
                    soma=soma+int(num)
            #    print(linha+"="+soma)
                arq_escrita.write(str(soma)+'\n')
