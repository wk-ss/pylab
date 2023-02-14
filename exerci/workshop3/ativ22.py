dic={"matheus":["carro","moto"],
     'pedro':['bicicleta','moto'],
     'maria':['bicicleta','carro'],
     'jose':['carro','moto'],
     'tiago':['carro','bicicleta']}
ca=0
mo=0
bi=0
for c in dic:
    for j in dic[c]:
        if j=="carro":
            ca+=1
            dic[c][dic[c].index(j)]=50
        if j=="moto":
            mo+=1
            dic[c][dic[c].index(j)]=25
        if j=="bicicleta":
            bi+=1
            dic[c][dic[c].index(j)]=10
    
print(f"carro ={ca}")
print(f"moto={mo}")
print(f"bicicleta={bi}")