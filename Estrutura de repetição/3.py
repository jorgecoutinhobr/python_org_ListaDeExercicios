n = str(input('Digite seu nome: ')).strip()
while len(n) < 3:
    n = str(input('Digite seu nome: ')).strip()
b = int(input('Digite sua idade: '))
while b < 0 or b > 150:
    b = int(input('Digite sua idade: '))
c = float(input('Digite seu salário: '))
while c < 0:
    c = int(input('Digite seu salário: '))
d = str(input('Digite F se for mulher ou M se for homem: ')).upper()
while d !='F' and d != 'M':
    d = str(input('Digite F se for mulher ou M se for homem: ')).upper()
e = str(input('Digite seu estado civil: [s], [c], [v] ou [d]  ')).upper()
while e != 'S' and e != 'C' and e != 'V' and e != 'D':
    e = str(input('Digite seu estado civil: [s], [c], [v] ou [d]')).upper()
else:    
    print('Cadastro finalizado.')
