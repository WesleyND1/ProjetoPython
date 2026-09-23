# Algoritmo Calcular raízes de Função de 2° grau
import math

# Declarando as variáveis
A = 0.00
B = 0.00
C = 0.00

Delta = 0.00
Raiz1 = 0.00
Raiz2 = 0.00

# Inicio
a = float(input("Insira o valor do coeficiente A: "))
b = float(input("Insira o valor do coeficiente B: "))
c = float(input("Insira o valor do coeficiente C: "))

# Calculando o Delta
Delta = b ** 2 - 4 * a * c

# Calculando as raízes
Raiz1 = (-b + math.sqrt(Delta)) / (2 * a)
Raiz2 = (-b - math.sqrt(Delta)) / (2 * a)

print("Delta é:", Delta)
print("Raiz 1 é:", Raiz1)
print("Raiz 2 é:", Raiz2)
# Fim