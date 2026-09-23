# série com fatorial: 1/2! + 1/3! + ... 1/n!


n = int(input("Digite um número: "))

fatorial = 1
serie = 1

for i in range(1, n + 1):
    fatorial *= i
    serie += 1 / fatorial

print("Resultado:", serie)