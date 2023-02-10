tmulta=0
cont=0
n=int(input())
while (n!=999):
    
    multa=0
    if n>2:
        multa=((n-2)*12.89)
        tmulta+=multa
        cont+=1
    n=int(input())
print("%.2f" % tmulta)
print(cont)

