# Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria

ana = 1.10
maria = 1.50

anos = 0

#inicio
while ana <= maria:
    ana += 0.03
    maria += 0.02
    anos += 1

print("Serão necessários", anos, "anos.")
#fim