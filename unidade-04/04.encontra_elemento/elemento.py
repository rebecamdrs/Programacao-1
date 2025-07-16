n = int(input())
sequencia = input().split()

resposta = "não"
for numero in sequencia:
    if int(numero) == n:
        resposta = "sim"
        
print(resposta)