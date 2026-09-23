#  Soma série 1 + 2/3 + 3/5 + ... + 50/99

serie = 0

#inicio
for i in range(1, 51):
    denominador = 2 * i - 1
    serie += i / denominador

print("Resultado:", serie)
#fim