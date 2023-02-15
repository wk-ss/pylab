idmagro=0
idgordo=0
magro=0
gordo=0
n=int(input("qtd bois: "))
for c in range(n):
    
    id,peso=map(float,input().split())
    if magro==0 and gordo==0:
        gordo=peso
        idgordo=id
        magro=peso
        idmagro=id

    elif peso>gordo :
        gordo=peso
        idgordo=id

    elif peso<magro :
        magro=peso
        idmagro=id

print('Gordo: id: %d peso: %.2f Kg'%(idgordo,gordo))
print('Magro: id: %d peso: %.2f Kg'%(idmagro,magro))