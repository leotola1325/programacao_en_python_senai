def calculadora():
    #VARIAVEIS LOCAIS
    while True: 
        n1 = float(input('nº : '))
        op = input('+|-|*|/ : ')
        if op == '+':
            n2 = float(input('nº : '))
            print(f' resultado = {n1+n2}')
        elif op == '-':
            n2 = float(input('nº : '))
            print(f' resultado = {n1-n2}')
        elif op == '*':
            n2 = float(input('nº : '))
            print(f' resultado = {n1*n2}')
        elif op == '/':
            n2 = float(input('nº : '))
            print(f' resultado = {n1/n2}')
        else:
            print('digite algo valido')

calculadora()