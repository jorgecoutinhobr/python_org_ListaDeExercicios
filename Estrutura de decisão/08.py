a = float(input('Digite o preço do produto 1 em reais: '))
b = float(input('Digite o preço do produto 2 em reais: '))
c = float(input('Digite o preço do produto 3 em reais: '))
if a < b and a < c:
    print('Você deve escolher o produto 1.')
elif b < a and b < c:
    print('Você deve escolher o produto 2.')
elif c < a and c < b:
    print('Você deve escolher o produto 3.')
elif a == b and a < c:
    print('Você pode optar pelos produtos 1 ou 2.')
elif b == c and b < a:
    print('Você pode optar pelos produtos 2 ou 3.')
elif c ==a and c < b:
    print('Você pode optar pelos produtos 1 ou 3.')