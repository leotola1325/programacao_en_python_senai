# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    IDENTAÇÃO     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# identação == organização de acordo com a sintaxe da limguagem  == aninhamento

# if 10 > 2:
#     print('maior')
#     if 10 < 111:
#         print('menor')


# ~~~~~~~~~~~~~~~~~~~~~~~~      DESAFIOS    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1 Imprima uma mensagem de boas-vindas na tela.
# 2 Declare uma variável booleana verdadeiro com o valor True e imprima seu tipo
# 3 Imprima o resultado da multiplicação de dois números decimais de sua escolha
# 4 Imprima o resultado da divisão (/)de dois números inteiros de sua escolha.
# 5 Imprima o resultado da subtração de dois números inteiros de sua escolha
# 6 Imprima o resultado da divisão (//)inteira de dois números inteiros de sua escolha.
# 7 Imprima o resultado da multiplicação de 4 números decimais de sua escolha
# 8 Declare uma variável numero e atribua um número inteiro. Em seguida, imprima o dobro desse número
# 9 Crie um sistema de cadastro com as estruturas que vc já conhece(Use apenas input, print e variavel)




#1   ============================================================
print('Boas vindas')
 
#2   ============================================================
n1 = 50
n2 = 20


#3   ============================================================
nu1 = float(input("Digite um numero: "))
nu2 = float(input("Digite outro numero: "))

mult = nu1*nu2
print(f"a multiplicação dos valores e: {mult}")



#4   ============================================================
num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))

div = num1/num2
print(f"a divisão dos valores e: {div}")



#5   ============================================================
nume1 = float(input("Digite um numero: "))
nume2 = float(input("Digite outro numero: "))

sub = nume1-nume2
print(f"a subtração dos valores e: {sub}")



#6   ============================================================
numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))

div_inteiro = numero1//numero2
print(f"o resultado ad divisão inteiro e de: {div_inteiro}")


#7   ============================================================
number1 = float(input("Digite o primeiro numero: "))
number2 = float(input("Digite o segundo numero: "))
number3 = float(input("Digite o terceiro numero: "))
number4 = float(input("Digite o quarto numero: "))

mult_quatro = number1*number2*number3*number4
print(f"o resultado da multiplicação dos 4 numeros é: {mult_quatro}")


#8   ============================================================
uno = int(input("dgite um numero: "))
dobro = uno*2

print(f"o dobro de {uno} é: {dobro} ")



# ~~~~~~~~~~~~~~~~~~~~~~~~    exercio com o meu aprendizado    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]


not1 = int(input("digite a primeira nota: "))
not2 = int(input("digite a segunda nota: "))
not3 = int(input("digite a terceira nota: "))
not4 = int(input("digite a quarta nota: "))

media = (not1+not2+not3+not4)/4

if media >= 7:
    print(f'''
    PARABENS voce foi aprovado 
    sua media foi {media} que esta esta muito boa
    ''')
elif media >=5:
    print(f'''
    hmmmm voce esta em recuperação
    sua media foi {media} que esta razoalmente aceitavel 
    ''')
else:
    print(f'''
        QUE PENA voce foi reprovado  
    sua media foi {media} mellhore o quanto possivel 
    ''')