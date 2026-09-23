# Receber a base e expoente e calcular a potência

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

#inicio
for i in range(expoente):
    resultado *= base

print("Resultado:", resultado)
#fim