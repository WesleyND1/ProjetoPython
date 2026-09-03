# Algoritmo para Calcular a Quantidade de Litros gastos em uma viagem

#Declarando as variáveis
litrosGasto = 0
tempoPercurso = 0
VelocidadeMedia = 0

#Inicio
tempoPercurso = float(input("Insira o tempo do trajeto em horas: "))
VelocidadeMedia = float(input("Insira a velocidade média em km/h: "))

litrosGasto = (tempoPercurso * VelocidadeMedia) / 12

print("Foram gastos", litrosGasto, "litros na viagem.")
#Fim