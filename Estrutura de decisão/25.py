a = int(input("Telefonou para a vítima? 1-sim 0-não " ))
b = int(input("Esteve no local do crime? 1-sim 0-não "))
c = int(input("Mora perto da vítima? 1-sim 0-não "))
d = int(input("Devia para a vítima? 1-sim 0-não "))
e = int(input("Já trabalhou com a vítima? 1-sim 0-não "))
x = a + b + c + d + e
if x == 2:
    print('SUSPEITO')
elif x >= 3 and x <= 4:
    print('Cúmplice.')
elif x ==5:
    print('Culpado')
else:
    print('Inocente')