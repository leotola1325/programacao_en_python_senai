# ===========================   media de alunos  =================================

# n1 = int(input("Digite primeira nota: "))
# n2 = int(input("Digite segunda nota: "))
# n3 = int(input("Digite terceira nota: "))

# media = (n1+n2+n3)/3

# if media >=7:
#     print("voce foi aprovado")
# elif media >=5:
#     print("voce esta em recuperação")
# else:
#     print("voce esta reprovado")

#  ============================= teste  sinais logicos ============================

#  n1 =10
#  n2 = 2

#  print(n1 > n2)   #maior                       ==  true (vdd)
#  print(n1 < n2)   #menor                       ==  false
#  print(n1 >= n2)  #maior ou igual              ==  true
#  print(n1 <= n2)  #menor ou igual              ==  false
#  print(n1 ! n20)  #diferente                   ==  true
#  print(n1 == n2)  #igual                       ==  false


# =============================== concatenar   =================================

# nome  = input("digite seu nome:  ")
# idade = int(input("digite sua idade: "))
# endereço  = input("digite seu endereço:  ")
# curso  = input("curso:  ")
# salario = float(input("digite seu salaro:  "))


# print('nome: ', nome)
# print('idade: ', idade)
# print('enderço: ', endereço)       #------->  forma com virgula
# print('curso: ', curso)
# print('salario: ', salario)


# print(f'''
# nome: {nome}
# idade: {idade}
# endereço: {endereço} 
# curso: {curso}
# salario: {salario}
# ''')
# # forma de pular linha =    \n   f'''    ''' --------> principais 

# print(f'leo: {nome}\n   yasmin: {nome}\n')




# ========================== desafios ======================================
# 1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.
# 2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.
# 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.
# 4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.
# 5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado. 


#1 
print(" ==================  resultado ao quadrado  ===================")
numero = int(input("digite um numero: "))
quadrado = numero**2

print(f"o numero: {numero} elevado ao quadrado resulta em: {quadrado} ")


#2
print(" ==================   nome completo  ===================")
nome = input("digite seu nome: ")
sobrenome = input("digite seu sobrenome: ")

print(f" seu nome completo e:  {nome} {sobrenome} ")

#3
print(" ==================   transformar inteiros em str  ===================")
n1 = int(input('numero inteiro: '))
n2 = int(input('numero inteiro: '))
print(str(n1),str(n2))


#4
print(" ==================   python  =================== ")
palavra = 'python'
num = int(input("digite um numero "))
print(f'{palavra}{num}')

#5

print(" ==================   digite final da frase  ===================\n era uma vez ... ")
frase = ' era uma vez '
final = input("digite a final da frase:  ")

print(f" {frase}{final}")