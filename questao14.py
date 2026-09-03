# Algoritmo Calcular o Valor do Terceiro Ângulo de Triângulo

#Declarando as variáveis
a1 = 0
a2 = 0
a3 = 0

#Inicio
a1 = float(input("Insira o valor do primeiro ângulo: "))
a2 = float(input("Insira o valor do segundo ângulo: "))

a3 = 180 - (a1 + a2)
print("O valor do terceiro ângulo é: ", a3, " graus")
#Fim