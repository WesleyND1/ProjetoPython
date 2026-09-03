# Algoritmo Calcular Volume de um Paralelepípedo

#Declarando as variáveis
comprimento = 0.00
largura = 0.00
altura = 0.00
volume = 0.00

#Inicio
print("Cálculo do Volume de um Paralelepípedo")
comprimento = float(input("Digite o comprimento em metros: "))
largura = float(input("Digite o largura em metros: "))
altura = float(input("Digite o altura em metros: "))

volume = (comprimento * largura * altura)
print("O volume é: ", volume, "m³")
#Fim