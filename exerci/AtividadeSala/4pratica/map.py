# I=list(map(int,L))
# print(list(map(lambda x:x+1,I)))
import csv
empregados={}

with open('empregados.cvs') as f:
    reader=csv.reader(f,delimiter=";")
    for l in reader:
        print(l)
    # for linha in f:
    #     partes=linha.strip().split(';')