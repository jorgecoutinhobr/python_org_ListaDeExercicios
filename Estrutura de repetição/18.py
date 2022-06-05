
while True:
    k = str(input('''DESEJA FAZER A OPERAÇÃO?
    SIM - [1]
    NÃO - [2]  ''')).strip()
    if k == '1':
        x = int(input('Quantos números diferentes você vai usar na sua operação? '))
        cont = 0
        p = 0
        m = 0
        for i in range(1, x+1):
            n = int(input('Digite um valor: '))
            cont += n
            if i == 1:
                p = n
                m = n
            if p > n:
                p = n
            if m < n:
                m = n
        print(cont, p, m)
        
    elif k != '1' and k != '2':
         k = str(input('''DESEJA FAZER A OPERAÇÃO?
    SIM - [1]
    NÃO - [2]  ''')).strip()
        
    else:
        print('-'*10 + 'FIM' + '-'*10)
        break

      

