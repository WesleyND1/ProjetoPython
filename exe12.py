# Algoritmo Calcular Idade

#Declarando as variáveis
# F representa Futuro

F = 0
idade = 0
anoAtual = 0
anoNascimento = 0

#Inicio
anoAtual = int(input("Digite o ano atual: "))
anoNascimento = int(input("Digite sua data de nascimento: "))

idade = (anoAtual - anoNascimento)
F = (anoAtual + 17)

print("Você possui ", idade, "anos")
print("E daqui a 17 anos você terá", F, "anos")
#Fim