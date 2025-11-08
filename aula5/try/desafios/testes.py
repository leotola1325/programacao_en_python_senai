#1 peça para usuario para inserir um numero a exceção caso ela insira algo que não seja um numero inteiro

try:
    n = int(input('digite um numero inteiro : '))

except ValueError as error:
    print(f' ERROR: {error} digite um numero inteiro ')
else:
    print('sem nenhum erro')
    
#2 peça para o usuario inserir dois nuemeros uma operação. manipulada e excesão caso o ocorra um erro na operação  -  ZeroDivisionError
try:
    nummero1 = float(input('digite um numero: '))
    nummero2 = float(input('digite um numero: ')) 

    divisao = nummero1 / nummero2

except ZeroDivisionError as error:
    print(f'error : {error}')
except ValueError as error:
    print(error)
else:
    print(f'resultado: {divisao}')
    
#3 crie uma lista e um idice como entrada e retorne o indice. manipile a excesão caso o indice seja invalido(caso imprima um indice que não exista na lista)
try:
    lista = ['banana', 'laranja', 'mexirica', 'melancia', 'abacaxi']
    print('''
    0 - banana
    1 - laranja
    2 - mexirica
    3 - melancia
    4 - abacaxi
      
    ''')
    escolha = int(input('digite seu produto: '))
    print(lista[escolha])
except IndexError as error:
    print(f'ERROR: {error} (indice não existe)')
except ValueError as error:
    print(error)
