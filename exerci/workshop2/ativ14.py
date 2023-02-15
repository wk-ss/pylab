a=int(input("Digite a quantidade de votos do candidato A:"))
b=int(input("Digite a quantidade de votos do candidato B:"))
c=int(input("Digite a quantidade de votos do candidato C:"))
n=int(input("Digite a quantidade de votos nulos:"))
tvotos=a+b+c+n
aporc=(a/tvotos)*100
bporc=(b/tvotos)*100
cporc=(c/tvotos)*100
nporc=(n/tvotos)*100
print(f"Candidato A: {aporc :.3f} %")
print(f"Candidato B: {bporc:.3f} %")
print(f"Candidato C: {cporc:.3f} %")
print(f"Votos Nulos: {nporc:.3f} %")
