# Receber quatro números, colocar em ordem crescente
# o quarto dígito não precisa estar em ordem

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

# inicio
if n4 < n1 :
    print(n4, n1, n2, n3)
elif n4 > n1 and n4 < n2:
    print(n1, n4, n2, n3)
elif n4 > n2 and n4 < n3:
    print(n1, n2, n4, n3)
else:
    print(n1, n2, n3, n4)
# fim