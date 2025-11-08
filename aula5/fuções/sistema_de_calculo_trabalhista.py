# horas extras do trabalhador
import colorama
from colorama import Fore, Back, Style, init

init()
def valor_hora(salario, carga):
    return salario/carga


def hora_extra(valor_hora):
    return valor_hora * 1.5


def qua_hora_extra(hora_extra,quantidade):
    return hora_extra * quantidade


def salario_total(salario, qua_hora_extra):
    return salario +  qua_hora_extra


def sistema_rh():
    while True:    
        print('***SISTEMA RH***')
        salario = float(input('Salario: '))
        carga = float(input('Carga: '))
        hora_trab = valor_hora(salario, carga)
        print('HORA DO TRABALHADOR R$', round(hora_trab,2) )
        print('-------------------------------')
        extra_50 =  hora_extra(hora_trab)
        print('HORA EXTRA VALOR R$', round(extra_50,2))
        print('-------------------------------')
        quantidade_extra =  float(input('Quantidade extra: '))
        qua_hr_extra = qua_hora_extra(extra_50,quantidade_extra)   
        print('R$', round(quantidade_extra,2)) 
        print('-------------------------------')
        salario_t = salario_total(salario,qua_hr_extra)
        print('R$', round(salario_t, 2))



sistema_rh()


input('digiter para sair: ')


