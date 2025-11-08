import random

#1 - crie uma função para comparar 2 numero(par ou impar)
def comparação():
    number1 = int(input('digite um numero: '))
    number2 = int(input('digite um numero: '))
    des = number1%2
    des2 = number2%2
    if des == 0 and des2 == 0:
        print(f'os dois numeros {number1} e {number2} são pares')
    elif des == 0 :
        print(f'somente o numero {number1} e par')
    elif des2 == 0 :
        print(f'somente o numero {number2} e par')
    elif des > 0 or des2 > 0:
        print('os dois são impares')
    else:
        print("os dois são impares")
# comparação()


#2 - crie uma função para multiplicar 3 numeros 

def multiplicar():
    num1 = int(input('digite um numero: '))
    num2 = int(input('digite um numero: '))
    num3 = int(input('digite um numero: '))
    
    print(f'''
    =====  resultado ====
    
    {num1} x {num2} x {num3} = {num1*num2*num3}
    ''')
# multiplicar()

#3 - 
def elevado():
    numero = int(input('Digite um numero: '))
    elevar = int(input('digite um numero para elevar: '))
    print(f'''
    ======= resultado ======
    
    {numero} elevado a {elevar} = {numero**elevar}
          ''')
# elevado()

#4 - CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.
#aluno122
def mensagem():
    idade = int(input('digite sua idade: '))
    if idade == 18:
        print('voce ja e maior de idade yupiiiii')
    elif idade > 0 and idade <18 or idade >18:
        print('mensagem')
    else:
        print('digite uma idade valida')
# mensagem()




#  5 

def descobrir(ano, ano_nasc, mes):
    
    if mes < 11:
        cal =  (ano  - ano_nasc   ) 
        print(cal)
    else:
        cal =  ano   -  1 -  (ano_nasc)
        print(cal)
# descobrir(2025,2000,10)            


#  6

def br(ano , lista):
    if ano in lista:
        print('O Brasil ganhou neste ano')

    else:
        print('Brasil não ganhou')


anos = [1958, 1962, 1970, 1994 , 2002.]

# br(1999,anos)            


# 7

def restaurante():
    produtos = ['macarronada', 'salada', 'sorvete', 'sanduiche']
    deseja_pedir = input('Deseja oedir')
     
    carrinho  = [] 

    while deseja_pedir == 'sim':
          produto =  int(input(f'produtos -> {produtos}'))
          carrinho.append(produtos[produto]) 
          print(carrinho)
        
          deseja_pedir = input('Deseja continuar? ')

    else:
        print('Obrigada volyte sempre!')              
# restaurante()        