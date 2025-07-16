tempo_disponivel = int(input())
qnt_avioes = int(input())
voos_autorizados = 0

for aviao in range(qnt_avioes):
    tempo_gasto = int(input())
    if tempo_disponivel >= tempo_gasto:
         tempo_disponivel -= tempo_gasto
          voos_autorizados += 1
 
print(f"{voos_autorizados} voo(s) autorizados.")