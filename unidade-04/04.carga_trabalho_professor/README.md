# Carga de trabalho do professor universitário

Teoricamente, segundo o regime T40, o professor deve dedicar 40 horas semanais para as atividades de ensino, pesquisa e extensão. Na prática, todavia, o professor universitário dedica mais do que isso. Isso acontece porque várias atividades não planejadas aparecem durante a semana. Na última estimativa que fez, um professor percebeu que, em média, ele trabalha 60 horas por semana, mas isso não é suficiente para realizar todas as atividades que lhe são atribuídas.

**Nesse contexto, faça um programa que leia uma sequência de duração de atividades (em horas) e registre essas atividades de acordo com a carga horária do professor. Esse professor em particular, decidiu que irá negar atividades cuja demanda seja maior que 10 horas. Além disso, caso atinja o limite (60 horas) o professor decreta “Fim de semana!”.**

## 📦 Entrada

- A entrada do programa consiste em uma sequência de N > 0 linhas, indicando a duração das atividades (em horas).  
- Atividades que demandam mais de 10 horas devem ser recusadas.  
- A leitura deve parar quando a soma dessas atividades for igual ou superior a 60, desconsiderando as atividades recusadas.

## 🌷 Saída

Na saída, seu programa deve imprimir a quantidade de atividades recusadas, bem como uma mensagem decretando o final de semana quando o limite for atingido. Veja os exemplos abaixo.


### ✅ Exemplo 1

```bash
# Entrada
10
10
10
10
10
10

# Saída
Rejeitadas = 0  
Fim de semana!
```

### ✅ Exemplo 2

```bash
# Entrada
10
12
10
8
15
6

# Saída
Rejeitadas = 2  
Fim de semana!
```
