#!/usr/bin/env python
# coding: utf-8

# In[1]:


url = 'https://raw.githubusercontent.com/rshernandez10/project-build-your-own-game/master/your-project/palabras.csv'


# In[2]:


import pandas as pd
import io
# palabrasdf = pd.read_csv(io.BytesIO(uploaded['palabras_.csv']))
palabrasdf = pd.read_csv(url)


# In[4]:


#print(palabrasdf)


# In[5]:


juego = palabrasdf.iloc[:,1].tolist()
#print(juego)


# In[6]:


def principal():

  import random
  import os

 # diccionario_palabras = []

  #palabras = ["COMPUTADORA" , "BALONES" , "AUDIFONO", "TECLADO", "ESCRITORIO", "GOLAZO", "NETFLIX",
 # "AHORCADO", "BICICLETA", "ATINADO", "TELESCOPIO"]

  palabra = list(random.choice(juego))

  #print(palabra)

  horca = ["          !=======|", #cuelga
          "                   |", #cabeza 
          "                   |", #brazos
          "                   |", #cuerpo
          "                   |", #piernas
          "    __________ ____|"] #pies

  ahorcado = ["          !=======|", #cuelga
              "          0       |", #cabeza 
              "         /|\      |", #brazos
              "          |       |", #cuerpo
              "         | |      |", #piernas
              "    _____-__-_____|"] #pies

  letras_todas = []
  fallos = 1

  resultado = []

  for i in range(len(palabra)):
      resultado.append("_")

  while True:
      os.system("cls")

      print ("                   ")
      print ("                   ")

      print ("******************")
      print ("**** AHORCADO ****")
      print ("******************")
      print ("                  ")
      print ("INSTRUCCIONES     ")
      print("Adivina la palabra, ingresando las letras de los espacios en blanco")
      print("Vocales sin acentos, ñ, o caracteres especiales")
      print("Tienes un máximo de 5 intentos")

  
      print ("                   ")
      print ("                   ")
      
      for i in range(fallos):
          print(ahorcado[i])
      for i in range(len(horca)-fallos):
          print(horca[i-fallos])

      print()

      print( "    ", end= "  ")
      for i in resultado:
            print(i, end=" ")

      print()
      print()

      if resultado == palabra:
          print("¡¡¡Has adivinado la palabra!!!")
          break
      
      if fallos > 5:
          print(" =( No has adivinado, la palabra es", "".join(palabra))
          print("Game Over")
          break
          
      while True:
          letra_usuario = input("Selecciona una letra: ") .upper()
          #letra_usuario = letra_usuario_sin_formato.upper()
          if len(letra_usuario) != 1: #si es distinto 
              print("No es una letra. Ingresa una letra nuevamente: ")
          elif letra_usuario in letras_todas:
              print ("Letra repetida. Ingresa otra: ")
          elif  letra_usuario not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
                print("No es una letra. Ingresa una letra nuevamente: ")
          else:
                letras_todas.append(letra_usuario)
                break

      for i in range(len(palabra)):
          if palabra[i] == letra_usuario:
              resultado[i] = letra_usuario

      if letra_usuario not in palabra:
          fallos += 1
    
      print()
      print()

  reiniciar = input("Jugar de nuevo? Oprime S para reiniciar u otra opcion para cerrar: ").upper()
  if reiniciar == "S":
    principal()
  else:
    exit()

principal()

