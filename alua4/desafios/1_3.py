# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.

# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

# 3*

# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.



#1
print(' =============   positivo, negativo ou zero  =================')
numero = float(input('digite um numero: '))

if numero == 0:
    print(f' seu numero e zero ')
elif numero > 0:
    print(f'seu numero e {numero}, e ele é positivo ')
else:
    print(f'seu numero é {numero}, e ele é negativo')

#2
print('================   Idade pra votar  ==============')
idade = int(input('Digite sua idade: '))

if idade > 60 or idade >= 16 and idade < 18:
    print('seu voto e opcional')
elif idade >= 18 and idade <= 60:
    print('Você é obrigado a votar.')
else:
    print('Você não pode votar.')
