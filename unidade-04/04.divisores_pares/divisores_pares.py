n = int(input())
for numero in range(1, n):
    if (n % numero == 0) and (numero % 2 == 0):
        print(numero)