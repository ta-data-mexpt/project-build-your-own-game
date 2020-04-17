import pygame
from pygame.locals import *
import sys
from random import randrange

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

AliceNonomura = Peleador(100,100,100,{'Golpe':50,'UpDefensa':25,'Descripcion':'Sube defensa propia'},'Alice Nonomura',1)
AlanGado = Peleador(80,100,120,{'Golpe':50,'DownDefensa':25,'Descripcion':'Baja defensa enemiga'},'Alan Gado',1)
YugoOgami = Peleador(120,80,100,{'Golpe':50,'UpAtack':25,'Descripcion':'Sube ataque propia'},'Yugo Ogami',1)
JennyBurtory = Peleador(100,120,80,{'Golpe':50,'DownAtack':25,'Descripcion':'Baja ataque enemigo'},'Jenny Burtory',1)

finalboss = Peleador(120,120,120,{'ata1':'ata1'},'Final Boss',1)

player = Peleador(0,0,0,{'ata1':'ata1'},'nombre',1)

peleadores = [AliceNonomura,AlanGado,YugoOgami,JennyBurtory]
FBlist=[finalboss]





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
            elif evento.type==KEYDOWN  and evento.key == evento.key==K_1:
                print ('click - choose chatacter NUBER 1')
                player = peleadores[0]
                #player.stats()
                peleadores.pop(0)
                gamedisplay.fill(black)
                set_players(player, peleadores)
                exit()
            elif evento.type==KEYDOWN  and evento.key == evento.key==K_2:
                print ('click - choose chatacter NUBER 2')
                player = peleadores[1]
                peleadores.pop(1)
                gamedisplay.fill(black)
                set_players(player, peleadores)
                exit()   
            elif evento.type==KEYDOWN  and evento.key == evento.key==K_3:
                print ('click - choose chatacter NUBER 3')
                player = peleadores[2]
                peleadores.pop(2)
                gamedisplay.fill(black)
                set_players(player, peleadores)
                exit()      
            elif evento.type==KEYDOWN  and evento.key == evento.key==K_4:
                print ('click - choose chatacter NUBER 4')
                player = peleadores[3]
                peleadores.pop(3)
                gamedisplay.fill(black)
                set_players(player, peleadores)
                exit()      
            elif evento.type==KEYDOWN:
                print ("nada")
                pass
            else:
                pass


def set_players(player, peleadores):
    num_peleadores = int((len(peleadores)))

    if num_peleadores >0 :
        #print ("-------PLAYER-------")
        #player.stats()
        #print ("-------PELEADORES-------")
        #print (("Numero de peleadores: ")+str(num_peleadores))
        #for i in peleadores:
        #    i.stats()
        
        sorteo = (randrange(0,num_peleadores))
        #print ("-------ENEMY-------")
        enemy = peleadores[sorteo]
        #enemy.stats()
        peleadores.pop(sorteo)
        #print ("-------PELADORES RESTANTES-------")
        #for i in peleadores:
            #i.stats()

        fight(player,enemy,peleadores)
        exit()
    else:
        print("NO HAY PELEADORES")


def fight(player,enemy,peleadores):
    fighting = player
    img_choose=pygame.image.load('choose_character.png')
    intro = True

    print ("------FIGHTER-----")
    fighting.stats()
    print ("------ENEMY-----")
    enemy.stats()
    print ("------PELEADORES-----")
    for i in peleadores:
        i.stats()

    while intro:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit
                quit()

        if evento.type==KEYDOWN  and evento.key == evento.key==K_1:
            print ('click -- first fight')            
            gamedisplay.fill(black)
            sys.exit()
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