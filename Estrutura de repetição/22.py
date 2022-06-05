n = int(input('Digite um numero inteiro: '))
cont = 0
for i in range(2, n):
    if n % i == 0:
        print(f'{i} é múltiplo de {n}')
        cont +=1
if cont == 0:
    print(f'É primo, pois {n} só divisivel por 1 e por ele mesmo.')
else:
    print('Ele não é primo.')