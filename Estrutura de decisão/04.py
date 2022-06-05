a = str(input('Digite uma letra para saber se ela é uma vagol ou consoante: ')).lower()
if a != 'a' and a != 'e' and a != 'i' and a != 'o' and a != 'u':
    print(f'{a} é consoante.')
else: 
    print('É vogal.')
