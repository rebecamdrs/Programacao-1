tamanho_sequencia = int(input())

contador = 0
for i in range(tamanho_sequencia):
    numero = int(input())
    if numero % 2 != 0:
        contador += 1

porcentagem = (contador * 100) / tamanho_sequencia
print(f"{contador} ({porcentagem:.1f}%)")