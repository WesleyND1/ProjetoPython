# Algoritmo Calcular o Valor da Hipotenusa
import math
#Declarando as variáveis
Cat1 = 0
Cat2 = 0
Hipotenusa = 0

#Inicio
Cat1 = float(input("Insira o valor do primeiro cateto: "))
Cat2 = float(input("Insira o valor do segundo cateto: "))

Hipotenusa = (Cat1 **2 + Cat2 **2)
Hipotenusa =  math.sqrt(Hipotenusa)

print("O valor da hipotenusa é: ", Hipotenusa)
#Fim