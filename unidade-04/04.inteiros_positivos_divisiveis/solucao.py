a = int(input())
b = int(input())
k = int(input())

for n in range(1, k + 1):
    if n % a == 0 and n % b == 0:
        print(n)