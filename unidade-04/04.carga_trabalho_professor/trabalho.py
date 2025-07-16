rejeitadas  = 0
horas_trabalho = 0

while (horas_trabalho < 60):
    hora_atividade = int(input())

    if hora_atividade > 10:
        rejeitadas += 1
    else:
         horas_trabalho += hora_atividade

print(f"Rejeitadas = {rejeitadas}")
print(f"Fim de semana!")