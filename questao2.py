#Algoritmo Reajuste de 15% do Salário

#Declarando as variáveis
Salario = 0.00
SalarioR = 0.00

#Inicio
Salario = float(input("Digite um salário: "))
SalarioR = Salario + (Salario / 100 * 15)
print("Salario com reajuste de 15% é: R$", SalarioR)
#Fim