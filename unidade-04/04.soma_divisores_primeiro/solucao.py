numero_ref = int(input())
soma = 0
for i in range(10):
    numero = int(input())
    if numero_ref % numero == 0:
        soma += numero
print(soma)