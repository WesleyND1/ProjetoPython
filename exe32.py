# Fatorial

n = int(input("Digite um número inteiro: "))

fatorial = 1

# inicio
for i in range(1, n + 1):
    fatorial *= i

print("Fatorial:", fatorial)
# fim