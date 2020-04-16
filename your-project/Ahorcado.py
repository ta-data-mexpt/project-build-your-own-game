import random
#Variable global
puntuacion_jugador=0
ganador=0
Imagenes_ahorcado=[ '''


========= 1''','''

|   
|   
|   
|
|
========= 2''','''
+---+
|   
|   
|
|
|
========= 3''','''
+---+
|   |
|   
|  
|  
|   
========= 4''','''
+---+
|   |
|   O
|  
|   
|   
========= 5''','''
+---+
|   |
|   O
|   |
|
|
=========6''','''
+---+
|   |
|   O
|  /|
|  
|   
=========7''','''
+---+
|   |
|   O
|  /|\
|  
|   
========= 8''','''
+---+
|   |
|   O
|  /|\
|  / 
|   
========= 9''','''
+---+
|   |
|   O
|  /|\
|  / \
|   
========= 10''']

Astronomia4=['luna','NASA','star','roja']
Astronomia5=['Marte','Venus','Space','Urano']
Astronomia10=['planetoide','telescopio','astronomia','planetaria']
Biologia4=['agua','raiz','alga','aves']
Biologia5=['cinco','genes','pulpo','golgi']
Biologia10=['sanguineos','nutrientes','citoplasma','aminoacido']

#funcion principal de juego 
def main():
    #Comienzo del juego; el usuario selecciona modo de juego
    
    jugadores=input('Selecciona el numero de jugadores escribe 1 ó 2:')
    rondas=input('Selecciona el numero de rondas escribe 1 ó 2:')
    dificultad=input('Selecciona la dificultad del juego: baja: 1 ,media: 2,alta: 3')
    tema=input('Selecciona la tematica de juego : Astronomía = 1, Biología =2, Random= 3')

    #Variables para ciclos y modo de juego
    rondas_completadas=0
    jugadores_finalizados=0
    
    #Crear primer ciclo para numero de jugadores, parara hasta que el numero de jugadores sea igual al seleccionado:
    while jugadores_finalizados < jugadores:
        jugadores_finalizados+=1
        
    #Segundo ciclo , finaliza hasta que el numero de rondas sea = al numero de rondaas seleccionadas
        while rondas_completadas < rondas:
            
            pistas(tema,dificultad)

            tablero(palabra,Imagenes_ahorcado)

    tablero_final()

            

#Algoritmo de juego
def tablero (palabra,Imagenes_ahorcado):
    
    tupalabra=" "
    
    intentos=10

    ronda_ganada=0
    
    while intentos > 0:
        
    fallas=0
    
    for letra in palabra:
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("_",end="")
            fallas+=1
            
        if fallas==0:
        input()
        print("")
        print("Ronda ganada")
        ronda_ganada=1
        input()
        return ronda_ganada

    tuletra=input("introduce una letra: ")
    tupalabra+=tuletra

    if tuletra not in palabra:
        intentos-=1
        print("equivocacion")
        print("tu tienes ",+intentos," vidas")
    if intentos== 0:
        print("perdiste!")
    

#Funcion para mostrar la pista de la palabra
def pistas(tema,dificultad):
    
    palabra_azar(tema,dificultad)
    
    if palabra == 'luna':
        return 'Quinto satelite más grande del sistema solar'
    elif palabra == 'Marte'
        return 'Segundo planeta más pequeño del Sistema Solar'

    return palabra
#Esta función , dependiendo el tema , lanzara la palabra para cada ronda
    
def palabra_azar(tema,dificultad):
    #Astronomia
    if tema==1 and dificultad==1:
        palabra=random.choice(Astronomia4)
        return palabra
    elif tema==1 and dificultad==2:
        palabra=random.choice(Astronomia5)
        return palabra
    elif tema==1 and dificultad==3:
        palabra=random.choice(Astronomia10)
    #Biologia
    elif tema==2 and dificultad==1:
        palabra=random.choice(Biologia4)
        return palabra
    elif tema==2 and dificultad==2:
        palabra=random.choice(Biologia5)
        return palabra
    elif tema==2 and dificultad==3:
        palabra=random.choice(Biologia10)
        return palabra
    #Random
    elif tema==2 and dificultad==1:
        Random4=Astronomia4+Biologia4
        palabra=random.choice(Random4)
        return palabra
    elif tema==2 and dificultad==2:
        Random5=Astronomia5+Biologia5
        palabra=random.choice(Random5)
        return palabra
    elif tema==2 and dificultad==3:
        Random10=Astronomia10+Biologia10
        palabra=random.choice(Random10)
        return palabra    
    
def pantala_juego(Imagenes_ahorcado,incorrecto,correcto,palabra_secreta):
    



        

    
    
