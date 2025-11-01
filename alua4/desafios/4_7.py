# 4*
# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

# print(' ================ medidas do triangulo   ==================')
# med1 = int(input("digite a 1° medida para criar um triangulo:  "))
# med2 = int(input("digite a 2° medida para criar um triangulo:  "))
# med3 = int(input("digite a 3° medida para criar um triangulo:  "))

# if  med1 == med2 == med3:
#     print('esse triangulo e equilátero')
# elif med1 == med2 or med1 == med3 or med2 == med3:
#     print('esse triangulo é isósceles')
# else:
#     print('esse triangulo e escaleno')


# 5*
# Determine se um número é múltiplo de 5 e 7.
n = int(input('Digite um número: '))

mult5 = n % 5
mult7 = n % 7

if mult5 == 0 and mult7 == 0:
    print(f'O número {n} é múltiplo de 5 e 7.')
elif mult5 == 0:
    print(f'O número {n} é múltiplo de 5.')
elif mult7 == 0:
    print(f'O número {n} é múltiplo de 7.')
else:
    print(f'O número {n} não é múltiplo de 5 nem de 7.')

# 6*
# Verifique se um número é positivo e maior que 10
# num = 19
# if num > 10:
#     print('o numero e positivo e maior de 10')
# elif num <0: 
#     print('esse numero e negativo ')
# else:
#     print('esse numero e menor que 10')
# Verifique se um número é divisível por 3 ou 5.