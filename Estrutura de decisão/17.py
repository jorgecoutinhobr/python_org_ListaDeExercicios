a = int(input('Digite um ano para avaliação: '))
if a % 4 == 0 and a % 100 != 0 or a % 100 == 0 and a % 400 ==0:
    print(f'O ano de {a} é bissexto.')
else:
    print(f'O ano de {a} não é bissexto')
