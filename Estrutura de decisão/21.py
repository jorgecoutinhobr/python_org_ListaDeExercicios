n = int(input('Digite o valor que você deseja sacar: APENAS INTEIROS - MÍNIMO DE 10 REAIS E MAXIMO DE 600 '))
cem = n//100
cinquenta = (n%100)//50
dez = (n%100%50)//10
cinco = (n%100%50%10)//5
um = (n%100%50%10%5)//1
print(f'''
NOTAS DE 100 [{cem}]
NOTAS DE 50 [{cinquenta}]
NOTAS DE 10 [{dez}]
NOTAS DE 5 [{cinco}]
NOTAS DE 1 [{um}]
''')

    



