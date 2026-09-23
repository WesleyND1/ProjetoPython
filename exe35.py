# Soma de valores ímpares entre dois números que o úsuario digitar 

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

soma = 0

for i in range(menor, maior + 1):
    if i % 2 != 0:
        soma += i

print("Soma dos ímpares:", soma)