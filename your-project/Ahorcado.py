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

#Esta función , dependiendo el tema , lanzara la palabra para cada ronda
def palabra_azar(palabras(tema,dificultad)):
    #Astronomia
    if tema==1 and dificultad==1:
        return random.choice(Astronomia4)
    elif tema==1 and dificultad==2:
        return random.choice(Astronomia5)
    elif tema==1 and dificultad==3:
        return random.choice(Astronomia10)
    #Biologia
    elif tema==2 and dificultad==1:
        return random.choice(Biologia4)
    elif tema==2 and dificultad==2:
        return random.choice(Biologia5)
    elif tema==2 and dificultad==3:
        return random.choice(Biologia10)
    #Random
    elif tema==2 and dificultad==1:
        Random4=Astronomia4+Biologia4
        return random.choice(Random4)
    elif tema==2 and dificultad==2:
        Random5=Astronomia5+Biologia5
        return random.choice(Random5)
    elif tema==2 and dificultad==3:
        Random10=Astronomia10+Biologia10
        return random.choice(Random10)
    

#Funcion para mostrar imagenes dependiendo palabra y dificultad
def pistas(palabra):
    if palabra == 'luna':
        return 'Quinto satelite más grande del sistema solar'
    elif palabra == 'Marte'
        return 'Segundo planeta más pequeño del Sistema Solar'
def pantala_juego(Imagenes_ahorcado,incorrecto,correcto,palabra_secreta):
    
   
def main():
    jugadores=input('Selecciona el numero de jugadores escribe 1 ó 2:')
    rondas=input('Selecciona el numero de rondas escribe 1 ó 2:')
    dificultad=input('Selecciona la dificultad del juego: baja: 1 ,media: 2,alta: 3')
    rondas_completadas=0
    jugadores_finalizados=0
    tema=input('Selecciona la tematica de juego : Astronomía = 1, Biología =2, Random= 3')

    #Crear primer ciclo para numero de jugadores, parara hasta que el numero de jugadores sea igual al seleccionado:
    while jugadores_finalizados < jugadores:
        jugadores_finalizados+=1
    #Segundo ciclo , finaliza hasta que el numero de rondas sea = al numero de rondaas seleccionadas
        while rondas_completadas < rondas:
            

            
    
def numero_jugadores(n):

def numero_rondas(n):


        

    
    
