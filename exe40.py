# Todos os primos exisentes entre 2 valores
# inicio
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

for numero in range(menor, maior + 1):

    if numero < 2:
        continue

    primo = True

    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
            break

    if primo:
        print(numero)
# fim