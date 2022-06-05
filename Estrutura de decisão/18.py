d = int(input('Digite um dia do mês: '))
m = int(input('Digite um mês do ano(em numeral): '))
a = int(input('Digite um ano(com 4 digitos): '))
if m == 1 or m == 3 or m == 5 or m ==7 or m ==8 or m ==10 or m ==12:
    if d<=31:
        print('Data válida.')
    else:
        print('Data inválida.')
elif m == 4 or m ==6 or m == 9 or m==11:
    if d <=30:
        print('DATA VÁLIDA')
    else:
        print('DATA INVÁLIDA')
elif m ==2:
    if a % 4 == 0 and a % 100 != 0 or a % 100 == 0 and a % 400 ==0:
        if d <=29:
            print('DATA VÁLIDA')
        else:
            print('DATA INVÁLIDA')
    else:
        if d <= 28:
            print('DATA VALIDA')
        else: 
            print('DATA INVÁLIDA')
    