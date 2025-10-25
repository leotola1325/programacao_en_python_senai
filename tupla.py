print(' ===================  Bem-Vindo  ========================')
print(f'''
      tenis nike = R$ 600,00
      camisa adidas = R$ 150,00
      fone = R$ 250,50
''')


e_comerce = {
    'tenis nike' : 600.0,
    'camisa adidas' : 150.0,
    'fone' : 250.50,
}

carrinho = []
valores = []

produto_1 = input('digite o nom do produto: ')
produto_2 = input('digite o nom do produto: ')

carrinho.append(produto_1)
carrinho.append(produto_2)
print(' ==============   seu carrinho   ==================')
print(carrinho)

valores.append(e_comerce[produto_1])
valores.append(e_comerce[produto_2])

print(f'R$ {valores}')
somar = sum(valores)
print(f'total = R${somar}')