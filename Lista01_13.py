minimo, maximo, real = int(input('Quantidade mínima para estoque: ')), int(input('Quantidade mínima para estoque: ')), int(input('Estoque real: '))
media = (minimo + maximo) / 2
if real < media:
    print('Necessário comprar!')
elif real > media:
    print('Não precisa adquirir novos produtos!')
else:
    print('Em breve será necessária aquisição de novos produtos!')
