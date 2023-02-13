#viagem de amigos

def pipa(quartos,pessoas):
    valorpessoa=pessoas*75
    if quartos==2:
        valorquartos=600
    elif quartos==3:
        valorquartos=900
    valort=valorquartos+valorpessoa
    valortp=valort/pessoas
    return valort,valortp

def fortaleza(quartos,pessoas):
    valorpessoa=pessoas*75
    if quartos==4:
        valorquartos=1120
    elif quartos==3:
        valorquartos=950
    valort=valorquartos+valorpessoa
    valortp=valort/pessoas
    return valort,valortp

pessoas=int(input(f"Digite a quantidade de pessoas:"))
desicao=int(input(f"Selecione a cidade escolhida: (1 - Pipa e 2 - Fortaleza)"))
quartos=int(input(f"Digite a quantidade de quartos:"))
if desicao==1:
    valores= pipa(quartos,pessoas)

    valort=valores[0]
    valortp=valores[1]

    print("Digite a quantidade de pessoas:")
    print("Selecione a cidade escolhida: (1 - Pipa e 2 - Fortaleza)")
    print("Digite a quantidade de quartos:")
    print(f"Valor total da viagem: R$ {float(valort)}")
    print(f"Valor por pessoa: R$ {float(valortp)}")
elif desicao==2:
    valores=fortaleza(quartos,pessoas)
    valort=valores[0]
    valortp=valores[1]
    print("Digite a quantidade de pessoas:")
    print("Selecione a cidade escolhida: (1 - Pipa e 2 - Fortaleza)")
    print("Digite a quantidade de quartos:")
    print(f"Valor total da viagem: R$ {float(valort)}")
    print(f"Valor por pessoa: R$ {float(valortp)}")