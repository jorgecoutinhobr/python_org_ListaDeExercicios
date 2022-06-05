t = 0
x = 1
y = 0
cont = 0
while cont < 14:
    cont += 1
    y = t + x
    t = x
    x = y
    print(y, end=' ')
print('-'*10  + 'FIM' + '-'*10)