a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
elif a == b and a > c:
    print(a)
elif b == c and b > a:
    print(c)
elif c == a and c > b:
    print(c)