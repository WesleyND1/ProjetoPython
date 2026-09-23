# Maior e menor valor entre 100 números

maior = 0
menor = 0

#inicio
for i in range(100):
    n = int(input("Digite um número positivo: "))

    if i == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n

        if n < menor:
            menor = n

print("Maior:", maior)
print("Menor:", menor)
# fim