# Básico - 32 canais e custa R$ 80.80
# Entretenimento - 55 canais e custa R$ 100.40
# Multicultural - 70 canais e custa R$ 130.23
# Completo - 112 canais e custa R$ 215.50


pacote = (str(input())).lower()
pagamento = (str(input())).lower()
preco = 0
canais = 0

if (pacote == 'básico'):
    if(pagamento != 'débito automático'):
        preco = 80.80
        canais = 32
    else:
        preco = 80.80*(0.95)
        canais = 32 + 6

if (pacote == 'entretenimento'):
    if(pagamento != 'débito automático'):
        preco = 100.40
        canais = 55
    else:
        preco = 100.40*(0.95)
        canais = 55 + 6

if (pacote == 'multicultural'):
    if(pagamento != 'débito automático'):
        preco = 130.23
        canais = 70
    else:
        preco = 130.23*(0.9)
        canais = 70 + 11
if (pacote == 'completo'):
    if(pagamento != 'débito automático'):
        preco = 215.50
        canais = 112
    else:
        preco = 215.50*(0.90)
        canais = 112 + 11


print('%.2f' %preco)
print(canais)