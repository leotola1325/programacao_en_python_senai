# lista  =  [1,2,3,4,5,6]


# l =  list(range(1,2000,10)) #  ------------> de 1 a 2000 pulando em 10 em 10
# print(l)


#1 - escreva um programa que use a função range() para gerar os pares de 2 a 20 e, eseguida imprima cada numero 
#2 - crie uma lista chamada  numeros que contenha os numeros inteiros de 1 a 10 e imprima na tela 
#3 - acesse e imprima o terceiro elemento da lista numeros 
#4 - adicione o numero 9 a lista numeros  e imprima a lista atualizada
#5 - remova o numero 5 da lista numeros e imprima a lista resultante

#1
print("====== lista pares =======")
pares = list(range(0,21,2))
print(pares)


#2
print(' =========== lista num =========')
numero = [1,2,3,4,5,6,7,8,9,10]
print(numero)
#3
print(numero[2])
#4
print('======= nova lista num =========')
numero.append(9)
print(numero)
#5
print('======= deletar 5 =========')
numero.remove(5)
print(numero)