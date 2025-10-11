lista = [1,2,3]
        #0 1 2  -----------------------> posições
print(lista[0])
lista[0] = 100

print(lista)


# ==================== funções e metodos ========================

#funções == nome_Da_função(lista)


#alguns que alteram 
#funções atribuir valores a lista

lista.append(10) # -----------> adicona um valor no final da lista
print(lista)

lista.insert(1,200) ##-------------> valor 
           #  |-----------> posição (1)

lista.extend([10,20,30,40,50]) #----------------> adicione varios valores porem no final da fila 

lista_+=(10,20,50,55,5)
print(lista_)

# remover os dados

lista_.pop() # remove de dentro pra fora 
print(lista_)

lista_.pop(5)
print(lista_)

lista_.remove(200)
print(lista_)

del lista_[0]
print(lista_)


# verificam um dado:



# tamanho

print(len(lista_))

# menor numero

print(min(lista_))

# maior numero

print(max(lista_))

# quanto tem de um dado 

print(lista_.count(10))

# ordenar a lista 

lista_.sort()
print(lista_)

# reverter a sequencia da lista 

lista_.sort(reverse = True)
print(lista_)

# copiar a lista 


x  =  lista_.copy()
print(x)

# limpar a lista
lista_.clear()
print(lista_)

# métodos
# nome.nomeMétodo



#  verificam um dado