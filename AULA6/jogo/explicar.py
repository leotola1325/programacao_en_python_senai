# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()


# o que a estrutura(sintaticamente)? para que serve(contexto)? 
# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/
# 1 - cita a estrutura de código
# 2 - contextualiza 




#exemplo:
# 2 varáveis , uma defini a aaltura a outra a largura 
largura, altura = 400, 400
tela = pygame.display.set_mode((largura, altura))  #------ modela o tamanho da tela de acordo com as variaveis 
pygame.display.set_caption("Labirinto") #  cria a janela do jogo com o nome


# variaveis de cores  de acordo com rgb
preto = (0, 0, 0) 
branco = (255, 255, 255)
vermelho = (255, 0, 0)

#definir tamamanho da cedula 
tamanho_celula = 40
labirinto = [                                                      # lista que determina o desing do mapa todos com o 1 terao blocos enquanto os == 0 serao onde o player podera andar 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],      # determinas os valores lista bidimensional 
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


x, y = 1 * tamanho_celula, 1 * tamanho_celula   #  2 variaveis pocionando as cedula
velocidade = 40 # variavel define velocidade da cedula

# função de desenhar o labirinto 
def desenhar_labirinto():
    for linha in range(len(labirinto)): #função de ler os valores da linhas do labirinto 
        for coluna in range(len(labirinto[linha])):#função de ler os valores das colunas com suas linhas  do labirinto 
            cor = preto if labirinto[linha][coluna] == 1 else branco  # condicional se  1 sera pintado de preto  se nao  sera pintado de branco  1 == preto  outro numero  == branco 
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula)) #criação do retangulo e suas medidas e pintando 

#loop infinito ate que suacondicional seja false
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:   # loopin  parao jogo so fechar quando a variavel for false
            executando = False

# dando funções para a as teclas   # estrutura fluxo de controle
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]: # caso aperte o botao de seta para esquerda  moverse para esquerda
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_RIGHT]:# caso aperte o botao de seta para direita  moverse para direita 
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_UP]:# caso aperte o botao de seta para cima  moverse para cima
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    if teclas[pygame.K_DOWN]:# caso aperte o botao de seta para baixo  moverse para baixo
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y


    tela.fill(branco)# cor do fundo ser usado a variavel branco

    #chamando as funções para serem usadas
    desenhar_labirinto()
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))
    pygame.display.flip()
    pygame.time.Clock().tick(10)

#função fechar o jogo
pygame.quit()
