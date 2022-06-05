a = 80000
b = 200000
taxaA = 0.03
taxaB = 0.015
anos = 0
t = int(input('Digite o numero de anos q vc quer analisar: '))
for i in range (1, t +1):
    a = a + (a * taxaA)
    b = b + (b * taxaB)
    anos += 1
print(f'Em {t} anos, a população "a" vai ser de {a:.2f} e a "b" vai ser de {b:.2f}.')