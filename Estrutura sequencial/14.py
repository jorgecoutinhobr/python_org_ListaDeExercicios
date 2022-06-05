peso = float(input('Quantos quilos voce pescou? '))
if peso <= 50:
    print('Sem excesso.')
else:
    excesso = (peso - 50) * 4
    print('Você deve pagar {} reais de multa.'.format(excesso))

   