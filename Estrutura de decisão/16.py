print('CALCULADORA DE SEGUNDO GRAU')
a = int(input('Digite um valor de a: '))
if a !=0:
    b = int(input('Digite um valor de b: '))
    c = int(input('Digite um valor de c: '))
    delta = (b**2 - 4*a*c)**0.5
    
    if delta != 0:
        finalp = (-b + delta)/(2*a)
        finaln = (-b-delta)/(2*a)
        print(f'{finalp:.2f}, {finaln:.2f}')
    
    elif delta == 0:
        finalp = (-b + delta)/(2*a)
        print(f'{finalp:.2f}')
    
    else:
        print('Delta não pode ser negativo --- FIM')
else:
    print('A não pode ser 0, pois isso faz com que a equação não seja de segundo grau!')