import math
metros = float(input('Digite o tamanho em m² da area a ser pintada: '))
litros = (metros / 3)
latas = math.ceil(litros / 18)
total = latas * 80
print(f'Você vai precisar de {latas} latas e isso vai custar {total} reais.')