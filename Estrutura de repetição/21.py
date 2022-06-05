n = int(input('Digite um numero inteiro: '))
cont = 0
for i in range(2, n):
    if n % i == 0:
        cont +=1
if cont == 0:
    print('É primo.')
else:
    print('Ele não é primo.')

