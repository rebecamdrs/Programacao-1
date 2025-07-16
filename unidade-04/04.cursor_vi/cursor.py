posicao_inicial = input().split()
linha = int(posicao_inicial[0])
coluna = int(posicao_inicial[1])

while True:
    comando = input().split()
    if comando == []:
        break
    repeticao = int(comando[0])
    letra = comando[1]

    if letra == 'h':
        coluna -= repeticao
    elif letra == 'j':
        linha += repeticao
    elif letra == 'k':
        linha -= repeticao
    else:
        coluna += repeticao
    print(f"[{linha} {coluna}]")