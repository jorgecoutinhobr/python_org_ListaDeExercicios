a = str(input('Você deseja abastecer com alcool(a) ou gasolina(g)? ')).lower()
l = float(input('Quantos litros você deseja colocar? '))
if a == 'a':
    if l <= 20:
        preco = l * (1.90 - (1.90 * 0.03))
        print(f'O valor pago será de {preco:.2f} reais.')
    elif l > 20:
        preco = l * (1.90 -(1.90 * 0.05))
        print(f'O valor pago será de {preco:.2f} reais.')
elif a == 'g':
    if l <= 20:
        preco = l * (2.5 - (2.50 * 0.04))
        print(f'O valor pago será de {preco:.2f} reais.')
    elif l > 20:
        preco = l * (2.5 - (2.50*0.06))
        print(f'O valor pago será de {preco:.2f} reais.')
    
