
quartos = ['','simples','duplo','luxo']
valores = [0,100,150,250]

pessoas = int(input('Quantas pessoas vão se hospedar (máx 3): '))


if pessoas > 3:
    pessoas = 3
    print("Só é permitido até 3 hóspedes. Considerando 3 pessoas.")

nomes = []
idades = []

for i in range(pessoas):
    nome = input(f'Nome da pessoa {i+1}: ')
    idade = int(input('Idade: '))
    nomes.append(nome)
    idades.append(idade)


for i in range(pessoas):
    print('Olá', nomes[i])

    escolha = int(input(f'''
escolha p seu quarto
1 - {quartos[1]} R$ {valores[1]}
2 - {quartos[2]} R$ {valores[2]}
3 - {quartos[3]} R$ {valores[3]}
'''))

    quantidade = int(input('Dias: '))
    calculo = valores[escolha] * quantidade

    print('R$', calculo)
    print('Dias', quantidade)

    formas_pag = ['', 'PIX','CC','CD']
    print(f'''
    1 - pix
    2 - cc
    3 - cd
    ''')
    pag = int(input('Forma de pagamento: '))
    print('forma de pagamento - ', formas_pag[pag])
    print('Obrigada volte sempre')
    print('--------------------------------')
