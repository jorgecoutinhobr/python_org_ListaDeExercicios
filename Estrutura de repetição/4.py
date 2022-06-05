a = 80000
b = 200000
taxaA = 0.03
taxaB = 0.015
anos = 0
while a<b:
    a = a + (a * taxaA)
    b = b + (b * taxaB)
    anos += 1
print(f'Vai levar {anos} anos para a alcançar b.')