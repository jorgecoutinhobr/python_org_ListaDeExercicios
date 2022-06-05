inteiro1 =  int(input('Digite um numero inteiro: '))
inteiro2 = int(input('Digite outro numero inteiro: ' ))
real = float(input('Digite um numero real: ' ))
a = (inteiro1 * 2) * (inteiro2 / 2)
b = (inteiro1 * 3) + real
c = round(real ** 3, 2)
print('O produto do dobro do primeiro com metade do segundo {}.'.format(a))
print('a soma do triplo do primeiro com o terceiro {}.'.format(b))
print('o terceiro elevado ao cubo {}.'.format(c))