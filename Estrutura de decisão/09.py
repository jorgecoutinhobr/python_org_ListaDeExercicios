a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero:: '))
c = float(input('Digite o terceiro numero:: '))
if a > b and b > c:
    print(a, b, c)
elif a > b and c > b:
    print(a, c, b)
elif b > a and a > c:
    print(b, a , c)
elif b > a and c > a:
    print(b, c, a)
elif c > a and a > b:
    print(c, a ,b)
elif c > a and b > a:
    print(c, b, a)
elif a == b and a < c:
    print(c, a, b)
elif b == c and c < a:
    print(a , c ,b)
elif c ==a and c < b:
    print(b, c , a)
