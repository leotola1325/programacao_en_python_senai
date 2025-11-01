print('=================   BEM-VINDO AO HOTEL   ===================')


nomes = []
idades = []
tipos_quarto = []
dias_clientes = []
totais = []

suites = {
    1: 100,   # Simples
    2: 150,   # Duplo
    3: 250    # Luxo
}


print('Cadastro de até 3 clientes:')



for i in range(3):
    print(f'Cliente {i+1}:')
    
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    
    nomes.append(nome)
    idades.append(idade)



print('''
Escolha o tipo de quarto:
1 - Simples = R$100/dia
2 - Duplo   = R$150/dia
3 - Luxo    = R$250/dia
''')


for i in range(3):
    print(f'Olá {nomes[i]}')
    
    tipo = int(input("Escolha o tipo de quarto (1, 2 ou 3): "))
    dias = int(input("Quantos dias ficará no hotel? "))


    tipos_quarto.append(tipo)
    dias_clientes.append(dias)


    preco = suites[tipo]
    total = preco * dias
    totais.append(total)

print(f'''
 {nomes[0]} seu total a pagar pela sua diaria de {dias_clientes[0]} é de  R${totais[0]}
 {nomes[1]} seu total a pagar pela sua diaria de {dias_clientes[1]} é de  R${totais[1]}
 {nomes[2]} seu total a pagar pela sua diaria de {dias_clientes[2]} é de  R${totais[2]}
''')
