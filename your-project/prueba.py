import time
lista=[ '''

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
nombre=input("como te llamas ")
print("hola, "+nombre," es hora de jugar")
print(" ")
time.sleep(1)
print("comienza a adivinar")
time.sleep(0.5)
palabra="murcielago"
tupalabra=" "
vidas=10

while vidas > 0:
    fallas=0
    for letra in palabra:
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("*",end="")
            fallas+=1
            
    if fallas==0:
        input()
        print("")
        print("felicidades, ganaste")
        input()
        break

    tuletra=input("introduce una letra: ")
    tupalabra+=tuletra


        
    if tuletra not in palabra:
        vidas-=1
        if vidas==9:
            print (lista[0])
        if vidas==8:
            print(lista[1])
        if vidas==7:
            print(lista[2])
        if vidas==2:
            print(lista[3])
        if vidas==6:
            print(lista[4])
        if vidas==5:
            print(lista[5])
        if vidas==4:
            print(lista[6])
        if vidas==3:
            print(lista[7])
        if vidas==2:
            print(lista[8])
        if vidas==1:
            print(lista[9])
    if vidas== 0:
        print(lista[-1])
        print("perdiste!")
        ganado=1
else:
    input()
    print("gracias por participar")
    input()
   
