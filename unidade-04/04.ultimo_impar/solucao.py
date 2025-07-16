numero = input()
qnt_impares = 0
ultimo_impar = 0

for digito in numero:
    if int(digito) % 2 != 0:
        qnt_impares += 1
        ultimo_impar = int(digito)

print(qnt_impares)
if qnt_impares == 0:
    print('-')
else:
    print(ultimo_impar)