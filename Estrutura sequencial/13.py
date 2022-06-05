sexo = input('Você é homem ou mulher? H ou M ')
altura = float(input('Digite sua altura: '))
if sexo == 'H':
   homem = round((72.7 * altura) - 58, 2)
   print('Seu peso ideal é de {} kg.'.format(homem))
else: 
    mulher = round((62.1 * altura) - 44.7, 2)
    print('Seu peso ideal é de {} kg.'.format(mulher))
