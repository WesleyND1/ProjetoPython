# Algoritmo Calcular Quantos Dias Durará o Alimento
# 50g de consumo ao dia
# Qa representa Quantidade de alimento
Qa = 0
dias = 0

#Inicio
Qa = int(input("Insira a quantidade de alimentos em kg: "))
dias = (Qa * 1000) / 50
print("O alimento irá durar ", dias, "dias")
#Fim