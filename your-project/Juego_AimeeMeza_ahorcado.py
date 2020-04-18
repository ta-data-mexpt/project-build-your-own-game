#Lanza una palabra al azar
import random
def palabra_azar(tema,dificultad):
    
    #ASTRONOMIA
    Astronomia1={'luna':'Quinto satelite más grande del sistema solar','marte':'Segundo planeta más pequeño del Sistema solar','roja':'La gigante___ es una estrella grande y fria','olimpus':'montaña más alta del Sistema Solar'}
    Astronomia2={'urano':'Descubierto por primera vez mediante un telescopio','alphacentauri':'Estrella más cercana al sistema solar','supernova':'explosión más grande que uno pudiera imaginarse','bigbang':'Se conoce como la gran explosión'}
    Astronomia3={'planetoide':'Tambien se le conoce como asteroide','telescopio':'Hubble','planeraria':'Es un tipo de nebulosa','quasar':'objeto muy lejano con mucha emisión de radiación'}
    
    #BIOLOGIA
    Biologia1={'raiz':'Lo primero en una germinación de una semilla','alga':'planta primitiva','agua':'Clave para  la vida','fungi':'reino de los hongos'}
    Biologia2={'genes':'Segmento de ADN','golgi':'El aparato de ___ esta en celular eucariontas','colibries':'conjunto de aves apodiformes endémicas de América','lombriz':'posee cinco pares de corazones'}
    Biologia3={'nutrientes':'Ayuda a las celulas con sus funciones vitales','citoplasma':'parte de celula','aminoacido':'molecula organica','anfibio':'una clase de vertebrados con respiración branquial'}
    
    #RANDOM
    Ra1=Astronomia1.copy()
    Ra2=Astronomia2.copy()
    Ra3=Astronomia3.copy()
    Rb1=Biologia1.copy()
    Rb2=Biologia1.copy()
    Rb3=Biologia1.copy()
    

    #Astronomia
    if tema==1 and dificultad==1:
        palabra=random.choice(list(Astronomia1.keys()))
        Frase = Astronomia1.get(palabra)
        return palabra,Frase
    elif tema==1 and dificultad==2:
        palabra=random.choice(list(Astronomia2.keys()))
        Frase = Astronomia2.get(palabra)
        return palabra,Frase
    elif tema==1 and dificultad==3:
        palabra=random.choice(list(Astronomia3.keys()))
        Frase = Astronomia3.get(palabra)
        return palabra,Frase
    
    #Biologia
    elif tema==2 and dificultad==1:
        palabra=random.choice(list(Biologia1.keys()))
        Frase = Biologia1.get(palabra)
        return palabra,Frase
    elif tema==2 and dificultad==2:
        palabra=random.choice(list(Biologia2.keys()))
        Frase = Biologia2.get(palabra)
        return palabra,Frase
    elif tema==2 and dificultad==3:
        palabra=random.choice(list(Biologia3.keys()))
        Frase = Biologia3.get(palabra)
        return palabra,Frase
    
    #Random
    elif tema==3 and dificultad==1:
        Ra1.update(Rb1)
        palabra=random.choice(list(Ra1.keys()))
        Frase = Ra1.get(palabra)
        return palabra,Frase
    elif tema==3 and dificultad==2:
        Ra2.update(Rb2)
        palabra=random.choice(list(Ra2.keys()))
        Frase = Ra2.get(palabra)
        return palabra,Frase
    elif tema==3 and dificultad==3:
        Ra3.update(Rb3)
        palabra=random.choice(list(Ra3.keys()))
        Frase = Ra3.get(palabra)
        return palabra,Frase

#Manda la pista de la palabra, esta funcion llama la funcion palabra_azar
def pistas(tema,dificultad,palabra_repetida):
    
    palabra,Frase=palabra_azar(tema,dificultad)
    
    while palabra in palabra_repetida:
        
        palabra,Frase=palabra_azar(tema,dificultad)
    
        
    return palabra,Frase

#Juego
def tablero(palabra,Frase):
    
    import time
    Imagenes=['''
        
      ========= 1''', '''
         
             |
             |
             |
             |
             |
      ========= 2 ''', '''

         +---+
             |
             |
             |
             |
             |
      ========= 3''', '''


         +---+
         |   |
             |
             |
             |
             |
      ========= 4''', '''

     
        +---+
        |   |
        O   |
            |
            |
            |
      ========= 5''', '''

        +---+
        |   |
        O   |
        |   |
            |
            |
      ========= 6''', '''

        +---+
        |   |
        O   |
       /|   |
            |
            |
      ========= 7''', '''

        +---+
        |   |
        O   |
       /|\  |
            |
            |
      ========= 8''', '''

        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
      ========= 9''', '''



        +---+
        |   |
        O   |
       /|\  |
       / \  |
            | 
     ========= 10''']
        
    
    
 #   print("Hola, "+nombre)
    print('Comenzamos')
    print(Frase)
    print(" ")
    
    time.sleep(1)
    
    print("Start")
    
    time.sleep(0.5)
    
    tupalabra=" "
    
    vidas=10

    while vidas > 0:
        fallas=0
        for letra in palabra:
            if letra in tupalabra:
                print(letra,end="")
            else:
                print("_ ",end="")
                fallas+=1

        if fallas==0:
            
            print("")
            print("Felicidades, ganaste la ronda")
           
            ronda_ganada=1
            
            return ronda_ganada
            break

        tuletra=input("  introduce una letra: ")
        tupalabra+=tuletra



        if tuletra not in palabra:
            vidas-=1
            if vidas==9:
                print (Imagenes[0])
            if vidas==8:
                print(Imagenes[1])
            if vidas==7:
                print(Imagenes[2])
            if vidas==6:
                print(Imagenes[3])
            if vidas==5:
                print(Imagenes[4])
            if vidas==4:
                print(Imagenes[5])
            if vidas==3:
                print(Imagenes[6])
            if vidas==2:
                print(Imagenes[7])
            if vidas==1:
                print(Imagenes[8])
            if vidas== 0:
                print("perdiste!")
                print(Imagenes[9])
                print(' ')
                ronda_ganada=0
                return ronda_ganada
                break
              
def ganador(marcador):
    
    if marcador.index(max(marcador))==marcador.index(min(marcador)) and len(marcador) > 1:
        print('Empate')
        return
        
    print('Ganó el jugador:',marcador.index(max(marcador))+1)
#Funcion principal

def main():
    #Comienzo del juego; el usuario selecciona modo de juego
    print('***Bienvenido a Ahorcado****')
    print(' ')
    jugadores=int(input('Selecciona el numero de jugadores escribe 1 ó 2: '))
    print(' ')
    rondas=int(input('Selecciona el numero de rondas escribe 1 ó 2: '))
    print(' ')
    tema=int(input('Selecciona la tematica de juego : Astronomía = 1, Biología =2, Random= 3: '))
    print(' ')
    dificultad=int(input('Selecciona la dificultad del juego: baja=1 ,media=2,alta=3: '))
    print(' ')
  #crea lista del tamaño de numero de jugadores inicializados en 0
    marcador=[0]*jugadores
    palabras_repetidas=[]
    
    #Variables para ciclos y modo de juego
    rondas_completadas=0
    jugador=0
    #Crear primer ciclo para numero de jugadores, parara hasta que el numero de jugadores sea igual al seleccionado:
        
    while jugador < jugadores:
        print('*******')
        print('Eres el jugador',jugador+1)
        print(' ')
        rondas_completadas=0
        
        while rondas_completadas < rondas:
        
    #Segundo ciclo , finaliza hasta que el numero de rondas sea = al numero de rondaas seleccionadas
            
        
            palabra,Frase=pistas(tema,dificultad,palabras_repetidas)
            
            palabras_repetidas.append(palabra)
            
            puntuacion=tablero(palabra,Frase) 
            
            
            marcador[jugador]+=puntuacion
            
            rondas_completadas+=1

        jugador+=1
            
    ganador(marcador)

main()
