import math
area = float(input('Digite em m² a area ser pintada: '))
litros = ((area*1.1) / 6)
latas = math.ceil(litros / 18)
galao = math.ceil(litros / 3.6)
precol = latas * 80
precog = galao * 25
#compra lata x galão
latas2 = math.floor(litros / 18)
precol2 = latas2 * 80
sobra_litros = litros % latas2
galao_sobra = math.ceil(sobra_litros / 3.6)
precog2 = galao_sobra * 25
total = precol2 + precog2


print(f'''
[APENAS LATAS]
 - Serão usadas {latas} latas;
 - E o preço será de {precol} reais.

 [GALÕES]
 - Serão usados {galao} galões;
 - E o preço será de {precog} reais.

 [LATAS E GALÕES]
 - Serão usados {latas2} latas e {galao_sobra} galões;
 - E o preço será de {total}.
''')


  











   




