a = float(input('Digite o primeiro lado do triangulo: '))
b = float(input('Digite o segundo lado do triangulo: '))
c = float(input('Digite o terceiro lado do triangulo: '))
if a + b > c and a + c > b and b + c > a:
    print('É um triângulo.')
    if a == b and b == c:
        print('É um trângulo equilátero')
    elif a==b and b != c or a==c and c!=b or b==c and c != a:
        print('Triangulo isosceles')
    elif a != b and b != c and c != a:
        print('Tringulo escaleno')
else:
    print('Não é um triangulo.')

        



