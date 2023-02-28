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
"printar a primeria lista par"
for c in range(5):
    print(f'1par[{c}] = {par[c]}')
for ç in range(5):
    print(f'par[{ç}] = {par[ç]}')
par.clear()
"reutilizar a primeira lista par"
par.append(par2[:])
"printar a primeria lista imp"
for v in range(5):
    print(f'impar[{v}] = {impa[v]}')
impa.clear()
"reutilizar a primeira lista imp"
impa.append(imp2[:])
"print 2"
for b in range(len(impa)):
    print(f'impar[{b}] = {impa[b]}')
for n in range(len(par)):
    print(f'par[{n}] = {par[n]}')