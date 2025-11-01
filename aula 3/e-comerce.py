#  e-comerce

carrinho =[]
total = []

lista_produtos = ['','hd','ssd','iphone 17', 'pc dell']
valores_produtos = [0,500.50, 20.5, 7000.0, 8000.99]
print(f'''
1 - {lista_produtos[1]} = R${valores_produtos[1]}
2 - {lista_produtos[2]} = R${valores_produtos[2]}
3 - {lista_produtos[3]} = R${valores_produtos[3]}
4 - {lista_produtos[4]} = R${valores_produtos[4]}
''')

produto1 = int(input('ID do produto: '))
produto2 = int(input('ID do produto: '))
produto3 = int(input('ID do produto: '))


carrinho.append(lista_produtos[produto1])
print('Voce inseriu no seu carrinho -', carrinho)
total.append(valores_produtos[produto1])
print('R$',sum(total))


carrinho.append(lista_produtos[produto2])
print('Voce inseriu no seu carrinho -', carrinho)
total.append(valores_produtos[produto2])
print('R$',sum(total))

carrinho.append(lista_produtos[produto3])
print('Voce inseriu no seu carrinho -', carrinho)
total.append(valores_produtos[produto3])
print('R$',sum(total))


print (' ---------------------------')
print ('seu pedido ficou R$',sum(total))
print(carrinho)
print(' ----------------------------')

print(f'''
1 - Pix
2 - Cartão de Credito (CC)
3 - Cartão de Debito  (CD)
''')

forma_pag = ['','1 - Pix', '2 - CC', '3 - CD']
pag = int(input('escolha a forma de pagamento a partir do id '))
print('sua forma de pagamento é', forma_pag[pag], 'Obrigado volte sempre!')