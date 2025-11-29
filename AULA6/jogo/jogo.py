import pygame 



pygame.init()


tela =  pygame.display.set_mode([500,500])
run = True


while run:
      for eventos in pygame.event.get():
          if eventos.type  == pygame.QUIT:
               run = False     


      tela.fill('red')


      pygame.draw.rect(tela, 'green', (15,20,10,10))
      pygame.draw.rect(tela, 'green', (150,5,10,10))
      pygame.draw.rect(tela, 'green', (78,15,10,10))
      pygame.draw.rect(tela, 'green', (90,25,10,10))
      pygame.draw.rect(tela, 'green', (255,45,10,10))
      l =  [1,2,3]
      for x in l:
        pygame.draw.rect(tela, 'green', (78,300,10,10))
        pygame.draw.rect(tela, 'green', (90,325,10,10))
        pygame.draw.rect(tela, 'green', (255,228,10,10))
           


      


      pygame.display.flip()



pygame.quit()      