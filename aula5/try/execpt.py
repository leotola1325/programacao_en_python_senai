try:
    x  =  int(input('>')) 


    n = 10
    n2 = 2
    print(n/n2)
except ValueError as erro:
    print(erro)
except ZeroDivisionError as erro:
    print(erro)    
else:
    print('erro não identificado ')


finally:
    print('fim de carregamento... ')    



