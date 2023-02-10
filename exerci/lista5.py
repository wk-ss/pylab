n= int (input("tamanho:"))
while n<1:
    n=int (input("tamanho  invalido:"))
v1=[0]*n
v2=[0]*n
vres=[0]*n
for i in range (n):
    v1[i]=int (input(f"v1 elemento {i} :"))
for o in range (n):
    v2[i]=int (input(f"v2 elemento {i} :"))
    vres[i]= v1[i]+v2[i]
print(f" a soma dos vetores é {vres} ={v1}+{v2}")