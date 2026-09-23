# Fibonacci até o N-ésimo termo

n = int(input("Digite um número: "))

a = 0
b = 1

#inicio
for i in range(n):
    print(a)
    proximo = a + b
    a = b
    b = proximo
#fim