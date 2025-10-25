# **Exercício 0:** Escreva um programa que use a função `range()` para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.
# **Exercício 1:** Crie uma lista chamada numeros que contenha os números inteiros de 1 a 10 e imprima-a na tela.
# **Exercício 2:** Acesse e imprima o terceiro elemento da lista `numeros`.
# **Exercício 3:** Adicione o número 9 à lista `numeros` e imprima a lista atualizada.
# **Exercício 4:** Remova o número 5 da lista `numeros` e imprima a lista resultante.
# **Exercício 5:** Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado.



# exercio 0 - range

lista = list(range(2,21,2))
print(lista)

#exercicio 1 imprimir 
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)

#exercicio 2 
print(numeros[2])
#exercicio 3
numeros.append(9)
print(numeros)
#exercicio 4
numeros.remove(5)
print(numeros)
#exercicio 5

carros = ['fusca', 'ferrari', 'jeep']
print(carros,numeros)