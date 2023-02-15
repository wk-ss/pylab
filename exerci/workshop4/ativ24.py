
teclad1="qwertyuiopasdfghjkl;zxcvbnm,./"
def decriptarR(texto):
    base = 'qwertyuiopasdfghjkl;zxcvbnm,./'
    cripto = ''
    for word in texto:

        posicicao = base.find(word)

        posicicao -= 1

        if posicicao < 0:

            posicicao = len(base) - abs(posicicao)


        cripto = cripto + base[posicicao]
    return cripto
def decriptarl(texto):
    base = 'qwertyuiopasdfghjkl;zxcvbnm,./'
    cripto = ''
    for word in texto:

        posicicao = base.find(word)

        posicicao += 1

        if posicicao < 0:

            posicicao = len(base) - abs(posicicao)


        cripto = cripto + base[posicicao]
    return cripto


cifra=input()
texto=input()
cifra=cifra.lower()
if cifra=='r':
    k=decriptarR(texto)
    print(k)
if cifra=='l':
   l=decriptarl(texto)
   print(l)