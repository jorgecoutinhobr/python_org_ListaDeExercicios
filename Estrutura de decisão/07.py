a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
if a  >  b  and a > c:
    print(a)
    if b > c:
        print(c)
    elif c > b:
        print(b)
elif b > a and b > c:
    print(b)
    if a > c:
        print(c)
    elif c > a:
        print(a)
elif c > a and c > b:

    print(c)
    if a > b:
        print(b)
    elif c > a:
        print(a)
elif a == b and a > c:
    print(a, c)
elif b == c and b > a:
    print(b, a)
elif c==a and c > b:
    print(c, b)
