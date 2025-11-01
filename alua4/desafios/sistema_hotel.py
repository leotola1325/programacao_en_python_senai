# ***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.
# - *Cadastro de Cliente:*
# *O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*
# - *Reservas de Quartos:*
# ***O sistema deve oferecer 3 tipos de quartos:*** 
# ***"Simples", "Duplo" e "Luxo".***
# ***Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.***
# - ***Cálculo da Estadia:***
# ***O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***
# Exemplo: 
#  ***valor_cliente3 = preco_duplo * cliente3_dias***
# *Pagamento:*
# *O sistema deve exibir o valor total a ser pago por cada cliente.*

print('=================   bem vindo !!   ===================')

nome = []
idade = []

print('cadastro')
print('cliente 1')
nome1 = input('digite seu nome: ') 
idade1 = int(input('digite sua idade: '))
print('cliente 2')
nome2 = input('digite seu nome: ') 
idade2 = int(input('digite sua idade: '))
print('cliente 3')
nome3 = input('digite seu nome: ') 
idade3 = int(input('digite sua idade: '))

nome.append(nome1)
nome.append(nome2)
nome.append(nome3)

idade.append(idade1)
idade.append(idade2)
idade.append(idade3)
# print(nome,idade)
suites = {
    1 : 100,
    2 : 150,
    3 : 250
    }
print('''
    escolha seu quarto - (preço diaria) 
1 - simples = R$100,00
2 - Duplo =  R$150,00
3 - luxo =  R$250,00
''')
reservas = []

print(f'olá {nome[0]}: ')
qua1 = int(input('escolha seu tipo de quarto: '))
di1 = int(input('escolha a quantidade de dias: '))
print(qua1)
print(f'olá {nome[1]}: ')
qua1 = int(input('escolha seu tipo de quarto: '))
di1 =int(input('escolha a quantidade de dias: '))
print(f'olá {nome[2]}: ')
qua1 = int(input('escolha seu tipo de quarto: '))
di1 = int(input('escolha a quantidade de dias: '))

preco_total = qua1*di1
print(preco_total)
