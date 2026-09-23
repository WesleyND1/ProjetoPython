# Algoritmo Calcular Salário e Cada Dependente será acrescido R$100

#Declarando as variáveis
# Salário Líquido e Salário a Receber
salario = 0
salarioL = 0
salarioR = 0

hora = 0
valorPorHora = 0
percentualDesconto = 0
numeroDependentes = 0

#Inicio
hora = int(input("Insira as horas trabalhadas: "))
valorPorHora = int(input("Insira a valor por horas: "))
numeroDependentes = int(input("Insira a número de dependentes: "))
percentualDesconto = int(input("Insira o percentual de desconto: "))

salario = (hora * valorPorHora)
salarioL = salario - (salario * percentualDesconto / 100)
salarioR = salarioL + (numeroDependentes * 100)

print("O salário a receber é de: R$", salarioR)
#Fim