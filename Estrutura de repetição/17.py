k = 1
n = int(input('Digite um numero inteiro: '))
for i in range(n, 0, -1):
    k *= i
    print(i, end=' ')
print(f'= {k}', end='')