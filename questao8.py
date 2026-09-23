# Algoritmo Cálculo de Depósito em Poupança após 1 mês rendendo 1,3% a.m

#Declarando as variáveis
valorDeposito = 0
montante = 0

#Inicio
valorDeposito = float(input("Digite o valor depositado: R$"))
montante = valorDeposito + (valorDeposito * 0.013)
print("Após 1 mês de aplicação o montante é de: R$", montante)
#Fim