# Algoritmo Troca de valores de variáveis

#Declarando as variáveis
x = 0.00
y = 0.00

#Inicio
x = float(input("Digite um número: "))
y = float(input("Digite outro número: "))

x, y = y, x

print("O valor de x agora é: ", x)
print("E o valor de y agora é: ", y)
#Fim