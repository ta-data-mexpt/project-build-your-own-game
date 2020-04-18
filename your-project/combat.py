import pygame
from pygame.locals import *
import sys
from random import randrange
import pygame.font


pygame.init()

font = pygame.font.Font(None, 26)
gray=(119,118,110)
black=(0,0,0)
white=(255,255,255)
display_width=1100
display_height=600





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

    def hacerDano(self, fighting,enemy,peleadores):
        print ("Escogiste pegar")
        danio = (fighting.ataque  * fighting.ataque) / ( fighting.ataque + fighting.defensa )
        print ("Daño:" + str(danio))
        fighting.recibeDano(danio,enemy,peleadores)

    def hacerHechizo(self, fighting,enemy,peleadores):
        print ("Hechizo")
        danio = (fighting.ataque  * fighting.ataque) / ( fighting.ataque + fighting.defensa )
        print ("Daño:" + str(danio))
        fighting.recibeHechizo(danio,enemy,peleadores)
        pass

    def hacerConjuro(self, fighting,enemy,peleadores):
        print ("Conjuro")
        danio = (fighting.ataque  * fighting.ataque) / ( fighting.ataque + fighting.defensa )
        print ("Daño:" + str(danio))
        fighting.recibeConjuro(danio,fighting,enemy,peleadores)
        pass

    def recibeDano(self,danio,enemy,peleadores):
        print ("El enemigo recibe daño :" + str(danio))
        enemy.vida = (enemy.vida - danio)
        print (enemy.stats())
        fight(self,enemy,peleadores)
        pass

    def recibeHechizo(self,danio,enemy,peleadores):
        cual = (randrange(1,3))
        if cual ==1:
            print ("El enemigo recibe hechizo en ataque :" + str(danio))
            enemy.ataque = (enemy.ataque - danio)
            print (enemy.stats())
            fight(self,enemy,peleadores)
        elif cual==2:
            print ("El enemigo recibe hechizo en defensa :" + str(danio))
            enemy.defensa = (enemy.defensa - danio)
            print (enemy.stats())
            fight(self,enemy,peleadores)
        pass

    def recibeConjuro(self,danio,fighting,enemy,peleadores):
        cual = (randrange(1,3))
        if cual ==1:
            print ("El jugador recibe conjuro en ataque :" + str(danio))
            fighting.ataque = (fighting.ataque + danio)
            print (fighting.stats())
            fight(fighting,enemy,peleadores)
        elif cual==2:
            print ("El jugador recibe conjuro en defensa :" + str(danio))
            fighting.defensa = (fighting.defensa + danio)
            print (fighting.stats())
            fight(fighting,enemy,peleadores)
        pass


'''
El golpe a a disminuir la vida del oponente.
El conjuro afecta a quien lo llama, puede subir ataque o defensa de forma aleatoria
El hechizo afecta al enemigo, puede bajar  ataque o defensa de forma aleatorio
'''

AliceNonomura = Peleador(100,100,100,{'Golpe':50,'Conjuro':25,'Hechizo':25},'Alice Nonomura',1)
AlanGado = Peleador(80,100,120,{'Golpe':50,'Conjuro':25,'Hechizo':25},'Alan Gado',1)
YugoOgami = Peleador(120,80,100,{'Golpe':50,'Conjuro':25,'Hechizo':25},'Yugo Ogami',1)
JennyBurtory = Peleador(100,120,80,{'Golpe':50,'Conjuro':25,'Hechizo':25},'Jenny Burtory',1)

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
    text1 = font.render("1.  Nombre:  Alice Nonomura, Vida: 100, Ataque: 100,  Defensa: 100 ", 1, white)
    text2 = font.render("2.  Nombre:  Alan Gado, Vida: 80, Ataque: 100,  Defensa: 120 ", 1, white)
    text3 = font.render("3.  Nombre:  Yugo Ogami, Vida: 120, Ataque: 80,  Defensa: 100 ", 1, white)
    text4 = font.render("4.  Nombre:  Jenny Burtory, Vida: 100, Ataque: 120,  Defensa: 80 ", 1, white)
    intro = True
    while intro:
        gamedisplay.blit(img_choose,(0,0))
        gamedisplay.blit(text1,(200,200))
        gamedisplay.blit(text2,(200,250))
        gamedisplay.blit(text3,(200,300))
        gamedisplay.blit(text4,(200,350))
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
        credit()


def fight(player,enemy,peleadores):
    fighting = player
    asss=pygame.image.load('pelea.jpg')
    intro = True
    print ("------FIGHTER-----")
    fighting.stats()
    print ("------ENEMY-----")
    enemy.stats()
    #print ("------PELEADORES-----")
    #for i in peleadores:
    #    i.stats()
    while intro:
        gamedisplay.blit(asss,(0,0))
        pygame.display.update()
        clock.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit
                quit()

        if player.vida > 0 and enemy.vida >0:   
            print ("Puedes hacer estos movimientos")
            choose_mov(fighting,enemy,peleadores)
        elif enemy.vida<=0:
            print ("Habemus ganador")
            set_players(player,peleadores)
        elif player.vida<=0:
            print ("u loose")
            died()


def choose_mov(fighting,enemy,peleadores):
    intro = True
    print ("Movimientos: ",fighting.movimientos)

    while intro:
        
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit
                quit()
            elif evento.type==KEYDOWN  and evento.key == evento.key==K_1:                        
                print ("Golpe: ",fighting.movimientos['Golpe'])
                fighting.hacerDano(fighting,enemy,peleadores)
                
            elif evento.type==KEYDOWN  and evento.key == evento.key==K_2:
                print ("Conjuro: ",fighting.movimientos['Conjuro'])
                fighting.hacerConjuro(fighting,enemy,peleadores)

            elif evento.type==KEYDOWN  and evento.key == evento.key==K_3:
                print ("Hechizo: ",fighting.movimientos['Hechizo'])
                fighting.hacerHechizo(fighting,enemy,peleadores)
            elif evento.type==KEYDOWN:
                print ("nada")
                pass
            else:
                pass

'''
def second_fight():
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

#def final_boss():
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
'''
def credit():
    img_choose=pygame.image.load('youwin.png')

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