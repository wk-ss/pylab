alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
n = 0
m = 0

C = str(input()).upper()

for i in range(0, 26, 1):
    if (C == alfabeto[i]):
        posicao = i

for i in range(0, posicao + 1, 1):
    print('.' * (posicao - i), end='')
    while (n <= i):
        print(alfabeto[n], end='')
        n = n + 1
        m = i

    n = 0

    while (m >= 1):
        print(alfabeto[m - 1], end='')
        m = m - 1
    print('.' * (posicao - i), end='')
    print('')