cont = 0
par1 = 0
par2 = 0
imp1 = 0
imp2 = 0
while True:
    cont +=1
    if cont == 10:
        break
    i = int(input('Digite um numero: '))
    if i % 2 == 0:
        par1 += 1
    elif i % 2 != 0:
        imp1 +=1
    
print(f'São {par1} pares e {imp1} numeros impares.')