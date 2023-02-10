n= int (input("tamanho:"))
while n<1:
    n=int (input("tamanho  invalido:"))
v1=[0]*n
par=[0]*n
impar=[0]*n
qp=qi=0
for i in range (n):
    v1[i]=int (input(f"v1 elemento {i} :"))
    if v1[i] %2==0:
        par[qp]=v1[i]
        qp+=1
    else:
        impar[qi]=v1[i]
        qi+=1
par=par[:qp]
impar=impar[:qi]
print(f' lidos foram {v1} ,pares {par} ,impares {impar}')