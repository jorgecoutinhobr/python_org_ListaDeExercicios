kg_morango = float(input('Quantos kg de morango você quer? '))
kg_maca = float(input('Quantos kg de maçã você quer? '))
peso = kg_morango + kg_maca
preco_moran = 0
preco_maca = 0
preco_final = 0
if peso <= 5:
    preco_moran += 2.50
    preco_maca += 1.8
    totalmoran = preco_moran * kg_morango
    totalmaca = preco_maca * kg_maca
    preco_final = totalmaca + totalmoran
    print(preco_final)
elif peso > 5 and peso <=8:
    preco_moran += 2.20
    preco_maca += 1.5
    totalmoran = preco_moran * kg_morango
    totalmaca = preco_maca * kg_maca
    preco_final = totalmaca + totalmoran
    print(preco_final)
elif peso > 8 or preco_final > 25:
    preco_moran += 2.20
    preco_maca += 1.5
    totalmoran = preco_moran * kg_morango
    totalmaca = preco_maca * kg_maca
    preco_final = (totalmaca + totalmoran) - ((totalmaca + totalmoran) * 0.01)
    print(preco_final)

