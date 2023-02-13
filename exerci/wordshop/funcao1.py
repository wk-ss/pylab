def somar(a,b):

    return a+b
def maior(a,b):
    if a>b:
        return a
    else:
        return b
def menor(a,b):
    if a>b:
        return b
    else:
        return a

def sub(a,b):
    mai=maior(a,b)
    men=menor(a,b)
    return (mai-men)
    
a,b=map(int,input("digite a ou b:").split())
print(a,b)
print(maior(a,b))
print(menor(a,b))
print(sub(a,b))