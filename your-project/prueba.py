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
vidas=5

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
        if vidas==3:
            print (lista[0])
        if vidas==2:
            print(lista[3])
    if vidas== 0:
        print(lista[10])
else:
    input()
    print("gracias por participar")
    input()
