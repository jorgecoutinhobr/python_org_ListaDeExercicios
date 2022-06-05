n = int(input('Digite um numero inteiro: '))
m = int(input('Digite outro numero inteiro: '))
k = 0
if n < m:
    for i in range(n+1, m):
        k += i
if m < n:
    for i in range(m+1, n):
        k += i
print(f'A soma de todos os numeros inteiros entre {n} e {m} é de {k}.')