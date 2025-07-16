palavra = input()

resultado = "-"
for letra in palavra:
    if letra in "aeiouAEIOU":
        resultado = letra
        break
print(resultado)