par2=[]
imp2=[]
par=[]
impa=[]
contpar=0
contimp=0
for i in range(15):
    x=int((input("n:")))
    if x%2==0:
        if contpar>5:
            par2.append(x)
        else:
            par.append(x)
            contpar+=1
    else:
        if contimp>5:
            imp2.append(x)
        else:
            impa.append(x)
            contimp+=1
"printar a primeria lista"
for c in range(5):
    print(f'par[{c}] = {par[c]}')
par.clear()
"reutilizar a primeira lista"
for m in range(len(par2)):
    par.append(par2[m])
for v in range(5):
    print(f'impar[{v}] = {impa[v]}')
impa.clear()
for b in range(len(imp2)):
    impa.append(imp2[b])
    print(f'impar[{b}] = {impa[b]}')
for n in range(len(par)):
    print(f'par[{n}] = {par[n]}')
