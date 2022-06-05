
t = 0
x = 1
y = 0
cont = 0
n = int(input('Digite um numero para análise: '))
while cont < n:
    cont += 1
    y = t + x
    t = x
    x = y
    print(y, end=' ')
print('-'*10  + 'FIM' + '-'*10)
