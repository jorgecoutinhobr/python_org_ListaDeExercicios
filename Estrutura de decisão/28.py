carne =str(input('''
SEJA BEM VINDO AO MERCADO DA TROPA DO AINDA
                      
                      
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

CASO QUEIRA(SÓ É PERMITIDO ESCOLHER UM TIPO DE CARNE):
File Duplo - DIGITE A
Alcatra    - DIGITE B
Picanha    - DIGITE C\n

''')).lower()
kg = float(input('Digite quantos kg você deseja levar? '))
pagamento = str(input('Vai pagar usando o cartão da nossa loja? S-sim ou N-não ')).lower()
if carne == 'a':
    tipo = 'Filé duplo'
elif carne == 'b':
    tipo = 'Alcatra'
elif carne == 'c':
    tipo = 'Picanha'
if pagamento == 's':
    cartao = 'cartão da casa'
    if carne == 'a':
        if kg <= 5:
            total = (kg * 4.9) - ((kg * 4.9)*0.05)
            print(f'Você escolheu pagar com o {cartao}, escolheu {tipo} e o total vai ser de {total:.2f} reais.')
        else:
            total = (kg * 5.8) - ((kg * 5.8)*0.05)
            print(f'Você escolheu pagar com o {cartao}, escolheu {tipo} e o total vai ser de {total:.2f} reais.')
    elif carne == 'b':
        if kg <= 5:
            total = (kg * 5.9) - ((kg * 5.9)*0.05)
            print(f'Você escolheu pagar com o {cartao}, escolheu {tipo} e o total vai ser de {total:.2f} reais.')
        else:
            total = (kg * 6.8) - ((kg * 6.8)*0.05)
            print(f'Você escolheu pagar com o {cartao}, escolheu {tipo} e o total vai ser de {total:.2f} reais.')
    elif carne == 'c':
        if kg <= 5:
            total = (kg * 6.9) - ((kg * 6.9)*0.05)
            print(f'Você escolheu pagar com o {cartao}, escolheu {tipo} e o total vai ser de {total:.2f} reais.')
        else:
            total = (kg * 7.8) - ((kg * 7.8)*0.05)
            print(f'Você escolheu pagar com o {cartao}, escolheu {tipo} e o total vai ser de {total:.2f} reais.')
else:
    cartao = 'pagamento por cartão externo'
    if carne == 'a':
        if kg <= 5:
            total = (kg * 4.9) 
            print(f'Você escolheu pagar com o {cartao}, escolheu {tipo} e o total vai ser de {total:.2f} reais.')
        else:
            total = (kg * 5.8) 
            print(f'Você escolheu pagar com o {cartao}, escolheu {tipo} e o total vai ser de {total:.2f} reais.')
    elif carne == 'b':
        if kg <= 5:
            total = (kg * 5.9) 
            print(f'Você escolheu pagar com o {cartao}, escolheu {tipo} e o total vai ser de {total:.2f} reais.')
        else:
            total = (kg * 6.8) 
            print(f'Você escolheu pagar com o {cartao}, escolheu {tipo} e o total vai ser de {total:.2f} reais.')
    elif carne == 'c':
        if kg <= 5:
            total = (kg * 6.9) 
            print(f'Você escolheu pagar com o {cartao}, escolheu {tipo} e o total vai ser de {total:.2f} reais.')
        else:
            total = (kg * 7.8) 
            print(f'Você escolheu pagar com o {cartao}, escolheu {tipo} e o total vai ser de {total:.2f} reais.')

