letris = input("digite algo: ")

match letris: 
    case letris if letris == '':
        print('esta vazia')
    case _:
        print(f'à string na viavel que é : ({letris})')



# entendendo como funciona os case

# import random


# numero =  random.randint(1,6)
# match numero:
#     case 1:
#         print('😁')
#     case 2:
#         print('😈')
#     case 3:
#         print('🤡')
#     case 4:
#         print('😎')   
#     case 5:
#         print('🎃')   
#     case 6:
#         print('🤑') 




# n  =  int(input('Digite um numero: '))


# match n:
#     case 0:
#         print('Zero')
#     case n if n > 0:
#         print('positivo')
#     case n if n < 0:
#         print('Negativo')
#     case _:
#         print('Desconhecido')            