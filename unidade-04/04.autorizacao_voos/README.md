# Autorização voos

**Crie um programa que controla a decolagem de aviões em uma pista de aeroporto. Esse aeroporto, em particular, só funciona até um determinado horário. Portanto, dependendo do tempo que um avião demora para decolar, ele pode não ser autorizado.**

Você deve ler da entrada o tempo disponível para decolagens, o número de aviões que pretendem decolar e, respectivamente, o tempo que cada avião demora na decolagem. Seu programa deve contar a quantidade de voos autorizados.

Os aviões se posicionam na pista em fila. Caso seja autorizado, o avião decola e o tempo disponível diminui. Caso contrário, ele não decola e o próximo avião é analisado.

## 📦 Entrada
- A primeira linha da entrada indica o tempo (em minutos) disponível para decolagens.  
- A segunda linha contém uma quantidade N de aviões que pretendem decolar.  
- As N linhas subsequentes apresentam o tempo que cada avião demora para decolar. 
 
Abaixo temos um exemplo válido de entrada considerando **400 minutos** para decolagens, **4 aviões** na fila e, em seguida, o tempo necessário para a decolagem de cada avião.

```
400
4
100
200
500
1000
```

## 🌷 Saída
A saída é composta por apenas uma linha indicando a quantidade de voos autorizados.  
Um voo está autorizado se ainda há tempo suficiente para ele decolar.  
Para o exemplo de entrada acima temos a seguinte saída esperada:

```
2 voo(s) autorizados.
```

## ✅ Exemplo 
```bash
# Entrada
400
4
100
200
500
1000

# Saída
2 voo(s) autorizados.
```
