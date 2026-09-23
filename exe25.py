# Calcular tempo do jogo

hora_inicio = int(input("Hora de início: "))
min_inicio = int(input("Minuto de início: "))

hora_fim = int(input("Hora de final: "))
min_fim = int(input("Minuto de final: "))

inicio = hora_inicio * 60 + min_inicio
fim = hora_fim * 60 + min_fim

# inicio
if fim <= inicio:
    fim += 24 * 60

duracao = fim - inicio

horas = duracao // 60
minutos = duracao % 60

print("Duração total:", horas, "hora(s) e", minutos, "minuto(s)")
# fim