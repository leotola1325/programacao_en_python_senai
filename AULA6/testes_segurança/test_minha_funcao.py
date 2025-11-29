import minha_funcao
# test_minha_funcao.py


def testar():
    assert minha_funcao.funcao(10,20) == 30
    assert minha_funcao.funcao(50,30) == 80
    assert minha_funcao.funcao(100,50) == 150
    assert minha_funcao.funcao(2,3) == 5


def testar2():
    assert minha_funcao.funcao2(10,20) == -10
    assert minha_funcao.funcao2(50,30) == 20
    assert minha_funcao.funcao2(100,50) == 50
    assert minha_funcao.funcao2(2,3) == -1  


def testar3():
    assert minha_funcao.funcao3(10,20) == 200
    assert minha_funcao.funcao3(50,30) == 1500
    assert minha_funcao.funcao3(100,50) == 5000
    assert minha_funcao.funcao3(2,3) == 6