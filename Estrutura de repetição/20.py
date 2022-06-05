while True:
    t = str(input('''DESEJA FAZER A OPERAÇÃO?
    SIM - [1]
    NÃO - [2]  ''')).strip()
    if t == '2':
        print('-'*10, 'FIM', '-'*10)
    elif t != '1' and t != '2':
         t = str(input('''DESEJA FAZER A OPERAÇÃO?
    SIM - [1]
    NÃO - [2]  ''')).strip()
    else:
        k = 1
        n = int(input('Digite um numero inteiro positivo e menor que 16: '))
        
        
        while n < 0 or n > 16:
            n = int(input('Digite um numero inteiro positivo e menor que 16: '))

        if n > 0 and n < 16:
            for i in range(n, 0, -1):
                k *= i
                print(i, end=' ')
            print(f'= {k}')



