# Calcular série de 1/2 + 1/3 + ... 1/n

n = int(input("Digite N: "))

serie = 0

# inicio
for i in range(1, n + 1):
    serie += 1 / i

print("Resultado:", serie)
# fim