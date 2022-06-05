n1 = float(input('Digite o primeiro: '))
n2 = float(input('Digite o segundo: '))
op = str(input('Digite qual operação você deseja fazer? A, S, M or D')).lower()
if op == 'a':
    a = n1 +  n2
    if a % 2 == 0:
        print('Ele é par.')
    else:
        print('Ele é impar.')
    if a>0:
        print('Ele é positivo')
    else:
        print('Ele é negativo.')
    if a % 1 == 0:
        print('Ele é inteiro.')
    else:
        print('Ele é decima.l')
elif op == 's':
    a = n1 - n2
    if a % 2 ==0:
        print('Ele é par.')
    else:
        print('Ele é impar.')
    if a >0:
        print('Ele é positivo')
    else:
        print('Ele é negativo.')
    if a % 1 == 0:
        print('Ele é inteiro.')
    else:
        print('Ele é decimal')
elif op == 'm':
    a = n1 * n2
    if a % 2 ==0:
        print('Ele é par.')
    else:
        print('Ele é impar.')
    if a >0:
        print('Ele é positivo')
    else:
        print('Ele é negativo.')
    if a % 1 ==0:
        print('Ele é inteiro.')
    else:
        print('Ele é decima.l')
elif op == 'd':
    a = n1 / n2
    if a % 2 ==0:
        print('Ele é par.')
    else:
        print('Ele é impar.')
    if a >0:
        print('Ele é positivo')
    else:
        print('Ele é negativo.')
    if a % 1 ==0:
        print('Ele é inteiro.')
    else:
        print('Ele é decimal')
else:
    print('Inválido')
