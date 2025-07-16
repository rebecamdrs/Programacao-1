def conversor_letra(letra):
    diferenca = ord(letra) - 87
    return diferenca

hexadecimal = input()
tamanho = len(hexadecimal)
numerais = []

for i in range(tamanho):
    if hexadecimal[i].isdigit():
        numerais.append(int(hexadecimal[i]))
    else:
        numerais.append(conversor_letra(hexadecimal[i]))

decimal = 0
expoente = tamanho - 1

for numeral in numerais:
    produto = numeral * (16 ** expoente)
    decimal += produto
    print(f"{numeral} * 16^{expoente} = {produto}")
    expoente -= 1

print("---")
print(f"{hexadecimal}(16) = {decimal}(10)")