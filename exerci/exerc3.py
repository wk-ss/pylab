num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))

if num1 > num2:
    maior = num1
else:
    maior = num2
while (not(maior % num1 == 0 and maior % num2 == 0)):
     maior += 1 
print(maior)