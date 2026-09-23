# Número divisível por 2 e 3

n = int(input("Insira um número: "))

# inicio
if n % 2 == 0 and n % 3 == 0:
    print(n, " é divisível por 2 e 3")
elif n % 2 == 0:
    print(n, " só é dividível por 2")
elif n % 3 == 0:
    print(n, " só é divisível por 3")
else:
    print(n, " não é divisível por 2 e 3.")
# fim