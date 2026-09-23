# Grãos no Tabuleiro de xadrez

graos = 1
total = 0

# inicio
for casa in range(1, 65):
    total += graos
    print("Casa:", casa, "- Grãos:", graos)
    graos *= 2

print("Total de grãos:", total)
# fim