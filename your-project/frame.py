import pygame
from pygame.locals import *
import sys

pygame.init()

gray=(119,118,110)
black=(0,0,0)
display_width=1100
display_height=600


#danio= ('ataque'  * 'ataque' ) / ( 'ataque' + 'defensa' )

gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Combate por turnos")
clock = pygame.time.Clock()



class Peleador:
    def __init__(self,vida,defensa,ataque,movimientos,nombre,vivo):
        self.vida = vida
        self.defensa = defensa
        self.ataque = ataque
        self.movimientos = movimientos
        self.nombre = nombre
        self.vivo=True

    def stats(self):
        print ("Nombre: ",self.nombre , "\n"
               "Vida: ",self.vida , "\n" 
               "Ataque: ",self.ataque , "\n" 
               "Defensa: ",self.defensa , "\n" 
               "Movimientos:",self.movimientos , "\n"
               "Vive:",self.vivo , "\n" )

pl1 = Peleador(100,100,100,{'Golpe':50,'UpDefensa':25,'Descripcion':'Sube defensa propia'},'Alice Nonomura',1)
pl2 = Peleador(80,100,120,{'Golpe':50,'DownDefensa':25,'Descripcion':'Baja defensa enemiga'},'Alan Gado',1)
pl3 = Peleador(120,80,100,{'Golpe':50,'UpAtack':25,'Descripcion':'Sube ataque propia'},'Yugo Ogami',1)
pl4 = Peleador(100,120,80,{'Golpe':50,'DownAtack':25,'Descripcion':'Baja ataque enemigo'},'Jenny Burtory',1)

finalboss = Peleador(120,120,120,{'ata1':'ata1'},'Final Boss',1)

player = Peleador(0,0,0,{'ata1':'ata1'},'nombre',1)

peleadores = [pl1,pl2,pl3,pl4]
FBlist=[finalboss]
num_peleadores=len(peleadores)


def game_intro():
    img_intro=pygame.image.load('intro.png')

    intro = True

    while intro:
        for evento in pygame.event.get():
            #print (evento)
            if evento.type == pygame.QUIT:
                pygame.quit
                quit()

            elif evento.type==KEYDOWN and evento.key==K_ESCAPE:
                print ('click -- intro')
                gamedisplay.fill(black)
                game_start()    
                exit()
            
    
        gamedisplay.blit(img_intro,(0,0))
        pygame.display.update()

        clock.tick(50)

def game_start():
    img_start=pygame.image.load('start.png')

    intro = True

    while intro:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit
                quit()

            elif evento.type==KEYDOWN and evento.key==K_a:
                print ('click -- press any button')            
                gamedisplay.fill(black)
                choose_character()
                exit()

        gamedisplay.blit(img_start,(0,0))
        pygame.display.update()
        clock.tick(60)

def choose_character():
    img_choose=pygame.image.load('choose_character.png')

    intro = True
    while intro:

        gamedisplay.blit(img_choose,(0,0))
        pygame.display.update()
        clock.tick(60)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit
                quit()
            elif evento.type==KEYDOWN:
                print ("nada")
                pass

            while num_peleadores>0:
                print ('numero de peleadores')
                print (num_peleadores)
                sys.exit()

                if  evento.type==KEYDOWN  and evento.key == evento.key==K_1:
                    print ('click - choose chatacter NUBER 1')
                    print (peleadores)
                    player = peleadores[0]
                    peleadores.pop(0)
                    print (peleadores)
                    sys.exit()
                    gamedisplay.fill(black)
                    first_fight(player,pl2)
                    exit()
                else:
                    pass

def first_fight(player,enemy):
    fighting = player
    img_choose=pygame.image.load('choose_character.png')
    intro = True

    print ("------FIGHTER-----")
    fighting.stats()
    print ("------PLAYER-----")
    player.stats()
    print ("------ENEMY-----")
    enemy.stats()

    while intro:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit
                quit()
        click=pygame.mouse.get_pressed()
        if click[0]==1:
            print ('click -- first fight')            
            gamedisplay.fill(black)
            second_fight()
            exit()
        
        gamedisplay.blit(img_choose,(0,0))
        pygame.display.update()
        clock.tick(60)

#def second_fight():
    img_choose=pygame.image.load('choose_character.png')

    intro = True

    while intro:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit
                quit()

        click=pygame.mouse.get_pressed()
        if click[0]==1:
            print ('click -- sec fidght')            
            gamedisplay.fill(black)
            third_fight()
            exit()
    
        gamedisplay.blit(img_choose,(0,0))
        pygame.display.update()
        clock.tick(60)
    
#def third_fight():
    img_choose=pygame.image.load('choose_character.png')

    intro = True

    while intro:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit
                quit()

        click=pygame.mouse.get_pressed()
        if click[0]==1:
            print ('click-- third fight')            
            gamedisplay.fill(black)
            final_boss()
            exit()
    
        gamedisplay.blit(img_choose,(0,0))
        pygame.display.update()
        clock.tick(60)

def final_boss():
    img_choose=pygame.image.load('finalboss.png')

    intro = True

    while intro:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit
                quit()

        click=pygame.mouse.get_pressed()
        if click[0]==1:
            print ('click -- final boss')            
            gamedisplay.fill(black)
            credit()
            exit()
    
        gamedisplay.blit(img_choose,(0,0))
        pygame.display.update()
        clock.tick(60)

def credit():
    img_choose=pygame.image.load('credit.png')

    intro = True

    while intro:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit
                quit()

        click=pygame.mouse.get_pressed()
        if click[0]==1:
            print ('click -- credit')            
            gamedisplay.fill(black)
            died()
            exit()
    
        gamedisplay.blit(img_choose,(0,0))
        pygame.display.update()
        clock.tick(60)

def died():
    img_choose=pygame.image.load('died.png')

    intro = True

    while intro:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit
                quit()

        click=pygame.mouse.get_pressed()
        if click[0]==1:
            print ('click -- died')            
            gamedisplay.fill(black)
            game_start()
            exit()
    
        gamedisplay.blit(img_choose,(0,0))
        pygame.display.update()
        clock.tick(60)

game_intro()            