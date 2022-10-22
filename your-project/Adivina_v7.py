#!/usr/bin/env python
# coding: utf-8

import random
from unittest import result
import re 
import sys, time, os
import pyfiglet


# ****Simpsons****

# In[573]:


homero_simpson = {'Nombre':'Homero Simpson',
                  'Edad':'adulta',
                  'Pelo':'calvicie',
                   'Energía':'perezosa',
                   'Frase':"D'oh!",
                   'Ropa':'Jeans',
                   'Gustos':'cerveza',
                   'Sexo':'hombre'}
bart_simpson = {'Nombre':'Bart Simpson',
                  'Edad':'niñez',
                   'Pelo':'puntiagudo',
                   'Energía':'rebelde',
                   'Frase':'Multiplicate por cero',
                   'Ropa':'shorts',
                   'Gustos':'patineta',
                   'Sexo':'hombre'}
lisa_simpson = {'Nombre':'Lisa Simpson',
                  'Edad':'niñez',
                   'Pelo':'estrellado',
                   'Energía':'idealista',
                   'Frase':'Si alguien me necesita, estaré en mi abitacion.',
                   'Ropa':'vestido',
                   'Gustos':'saxofón',
                   'Sexo':'mujer'}
marge_simpson = {'Nombre':'Marge Simpson',
                  'Edad':'adulta',
                   'Pelo':'rizado',
                   'Energía':'estresada',
                   'Frase':'¡Hhmmmm...!',
                   'Ropa':'vestido',
                   'Gustos':'apostar',
                   'Sexo':'mujer'}
maggie_simpson = {'Nombre':'Maggie Simpson',
                  'Edad':'bebé',
                   'Pelo':'estrellado',
                   'Energía':'violenta',
                   'Frase':'N/A',
                   'Ropa':'vestido',
                   'Gustos':'armas',
                   'Sexo':'mujer'}
señor_burns = {'Nombre':'Señor Burns',
                  'Edad':'adulta',
                   'Pelo':'calvicie',
                   'Energía':'excéntrica',
                   'Frase':'Excelente',
                   'Ropa':'traje',
                   'Gustos':'poder',
                   'Sexo':'hombre'}
nelson_muntz = {'Nombre':'Nelson Muntz',
                  'Edad':'niñez',
                    'Pelo':'lacio',
                   'Energía':'destructiva',
                   'Frase':'No te golpees tú sólo',
                   'Ropa':'shorts',
                   'Gustos':'golpear',
                   'Sexo':'hombre'}
moe_syzslak = {'Nombre':'Moe Syzslak',
                  'Edad':'adulta',
                    'Pelo':'rizado',
                   'Energía':'suicida',
                   'Frase':'Los ricos no son felices. Desde el día en que nacen, hasta el día en que mueren, creen que son felices. Más créeme... no lo son.',
                   'Ropa':'pantalones',
                   'Gustos':'dinero',
                   'Sexo':'hombre'}
milhouse_vanhouten = {'Nombre':'Milhouse Van Houten',
                  'Edad':'niñez',
                    'Pelo':'lacio',
                   'Energía':'estudiosa',
                   'Frase':'¡Aaaaay mis anteojos!',
                   'Ropa':'shorts',
                   'Gustos':'videojuegos',
                   'Sexo':'hombre'}
ned_flanders = {'Nombre':'Ned Flanders',
                  'Edad':'adulta',
                    'Pelo':'lacio',
                   'Energía':'bondadosa',
                   'Frase':'¡Mi amiguillo, estoy de acuerdillo!',
                   'Ropa':'pantalones',
                   'Gustos':'Biblia',
                   'Sexo':'hombre'}


# **Game of thrones**

# In[574]:


jamie_lannister = {'Nombre' :'Jamie Lannister',
                    'Edad':'Adulto', 
                    'Casa':'Lannister', 
                    'Género':'Masculino', 
                    'Sobrevivio al final de la serie':'No', 
                    'Color de cabello':'Rubio', 
                    'Estatura':'Alto', 
                    'Con que letra empieza su nombre': 'J'}

tyrion_lannister = {'Nombre' :'Tyrion Lannister',
                    'Edad':'Adulto', 
                    'Casa':'Lannister', 
                    'Género':'Masculino', 
                    'Sobrevivio al final de la serie':'Si', 
                    'Color de cabello':'Castaño', 
                    'Estatura':'Baja', 
                    'Con que letra empieza su nombre': 'T'}

cersei_lannister = {'Nombre' :'Cersei Lannister',
                    'Edad':'Adulto', 
                    'Casa':'Lannister', 
                    'Género':'Femenino', 
                    'Sobrevivio al final de la serie':'No', 
                    'Color de cabello':'Rubio', 
                    'Estatura':'Media', 
                    'Con que letra empieza su nombre': 'C'}

aria_stark = {'Nombre' :'Aria Stark',
                  'Edad':'Niñ@-adolescente', 
                    'Casa':'Stark', 
                    'Género':'Femenino', 
                    'Sobrevivio al final de la serie':'Si', 
                    'Color de cabello':'Castaño', 
                    'Estatura':'Baja', 
                    'Con que letra empieza su nombre': 'A'}

sansa_stark = {'Nombre' :'Sansa Stark',
                    'Edad':'Niñ@-adolescente', 
                    'Casa':'Stark', 
                    'Género':'Femenino', 
                    'Sobrevivio al final de la serie':'Si', 
                    'Color de cabello':'Pelirojo', 
                    'Estatura':'Alta', 
                    'Con que letra empieza su nombre': 'S'}

bran_stark = {'Nombre' :'Bran Stark',
                    'Edad':'Niñ@-adolescente', 
                    'Casa':'Stark', 
                    'Género':'Masculino', 
                    'Sobrevivio al final de la serie':'Si', 
                    'Color de cabello':'Castaño', 
                    'Estatura':'Alta', 
                    'Con que letra empieza su nombre': 'B'}

john_snow = {'Nombre' :'John Snow',
                    'Edad':'Adolescente', 
                    'Casa':'No pertenecia a una casa', 
                    'Género':'Masculino', 
                    'Sobrevivio al final de la serie':'Si', 
                    'Color de cabello':'Negro', 
                    'Estatura':'Media', 
                    'Con que letra empieza su nombre': 'J'}

joffrey_baratheon = {'Nombre' :'Joffrey Baratheon',
                     'Edad':'Niñ@-adolescente', 
                    'Casa':'Baratheon', 
                    'Género':'Masculino', 
                    'Sobrevivio al final de la serie':'No', 
                    'Color de cabello':'Rubio', 
                    'Estatura':'Media', 
                    'Con que letra empieza su nombre': 'J'}

khal_drogo = {'Nombre' :'Khal Drogo',
                    'Edad':'Adulto', 
                    'Casa':'Dothraki', 
                    'Género':'Masculino', 
                    'Sobrevivio al final de la serie':'No', 
                    'Color de cabello':'Negro', 
                    'Estatura':'ALta', 
                    'Con que letra empieza su nombre': 'K'}


daenerys_targaryen = {'Nombre' :'Daenerys Targaryen',
                    'Edad':'Adolescente', 
                    'Casa':'Targaryen', 
                    'Género':'Femenino', 
                    'Sobrevivio al final de la serie':'Si', 
                    'Color de cabello':'Plata', 
                    'Estatura':'Media', 
                    'Con que letra empieza su nombre': 'D'}

caminantes_blancos =  {'Nombre' :'Caminantes Blancos',
                       'Edad':'Muy viejo', 
                    'Casa':'No tiene', 
                    'Género':'Femenino o masculino', 
                    'Sobrevivio al final de la serie':'No', 
                    'Color de cabello':'No tiene', 
                    'Estatura':'Variada', 
                    'Con que letra empieza su nombre': 'Puede empezar con muchas letras pero todos tienen ojos muy brillantes'}


# **Lord of the rings**

# In[575]:


Aragorn = {'Nombre':'Aragorn',
           'Edad':'Adulto', 
            'Reino':'Gondor', 
            'Género':'Masculino', 
            'Arma favorita':'Espada', 
            'Color de cabello':'Negro', 
            'Estatura':'Alta', 
            'Con que letra empieza su nombre':'A',
            'Raza' : 'Dunedain'}
    
Legolas = {'Nombre':'Legolas',
           'Edad':'Adulto', 
            'Reino':'Tierra media', 
            'Género':'Masculino', 
            'Arma favorita' :'Arco', 
            'Color de cabello':'Rubio', 
            'Estatura':'Alta', 
            'Con que letra empieza su nombre': 'L',
            'Raza' : 'Elfo'}

Gimli = {'Nombre':'Gimli',
         'Edad':'Adulto', 
            'Reino':'Aman', 
            'Género':'Masculino', 
            'Arma favorita' :'Hacha', 
            'Color de cabello':'Negro', 
            'Estatura':'Baja', 
            'Con que letra empieza su nombre': 'G',
            'Raza': 'Enano'  }

Sam =  {'Nombre':'Sam',
    'Edad':'Joven', 
            'Reino':'La comarca', 
            'Género':'Masculino', 
            'Arma favorita' :'Sartenes', 
            'Color de cabello':'Rubio', 
            'Estatura':'Baja', 
            'Con que letra empieza su nombre': 'S',
            'Raza': 'Hobbit'}

Frodo =  {'Nombre':'Frodo',
          'Edad':'Joven', 
            'Reino':'La comarca', 
            'Género':'Masculino', 
            'Arma favorita' :'No tiene', 
            'Color de cabello':'Castaño', 
            'Estatura':'Baja', 
            'Con que letra empieza su nombre': 'F',
            'Raza': 'Hobbit'}

Gollum = {'Nombre':'Gollum',
          'Edad':'Muy adulto', 
            'Reino':'Valles de Anduin', 
            'Género':'Masculino', 
            'Arma favorita' :'No tiene', 
            'Color de cabello':'No tiene', 
            'Estatura':'Baja', 
            'Con que letra empieza su nombre': 'G',
            'Raza': 'Originalmente hobbit'}
    
Galadriel = {'Nombre':'Galadriel',
             'Edad':'Adulta', 
            'Reino':'Tierra media - Lothlórien', 
            'Género':'Femenino', 
            'Arma favorita' :'No tiene perooo tiene ciertos poderes como predecir el futuro', 
            'Color de cabello':'Rubio', 
            'Estatura':'Alta', 
            'Con que letra empieza su nombre': 'G',
            'Raza': 'Elfo'}   
    
Boromir = {'Nombre':'Boromir',
           'Edad':'Adulto', 
            'Reino':'Gondor', 
            'Género':'Masculino', 
            'Arma favorita' :'Espada y tiene el Cuerno de Vorondil', 
            'Color de cabello':'Negro', 
            'Estatura':'Alta', 
            'Con que letra empieza su nombre': 'B',
            'Raza' : 'Hombre'}  
Gandalf =  {'Nombre':'Gandalf',
            'Edad':'Muy adulto', 
            'Reino':'Aman', 
            'Género':'Masculino', 
            'Arma favorita' :'Bastón Thranduil', 
            'Color de cabello':'Gris', 
            'Estatura':'Alta', 
            'Con que letra empieza su nombre': 'G',
            'Raza': 'Istar'}
    
    
    
Saruman =  {'Nombre':'Saruman',
            'Edad':'Muy adulto', 
            'Reino':'Isengard', 
            'Género':'Masculino', 
            'Arma favorita' :'Tiene una piedra vidente', 
            'Color de cabello':'Blanco', 
            'Estatura':'Alta', 
            'Con que letra empieza su nombre': 'S',
            'Raza': 'Istar'}

orcos  = {'Nombre':'orcos',
          'Edad':'Adulto', 
            'Reino': 'creados en Isengard', 
            'Género':'Masculino', 
            'Arma favorita' :'Espadas y sus dientes', 
            'Color de cabello':'Negro', 
            'Estatura':'Alta', 
            'Con que letra empieza su nombre': 'O',
            'Raza': 'Solian ser elfos'}


# **El padrino**

vito = {'Nombre':'Vito',
            'Apellido':'Corleone',
            'Puesto':'Don',
            'Físico':'barbilla salida',
            'Actor':'Marlon Brando',
            'Lugar de nacimiento':'Siciia',
            'Sexo':'hombre',
            'Personalidad':'líder'
            }

michael = {'Nombre':'Michael',
            'Apellido':'Corleone',
            'Puesto':'Don',
            'Físico':'nariz grande',
            'Actor':'Al Pacino',
            'Lugar de nacimiento':'Nueva York',
            'Sexo':'hombre',
            'Personalidad':'calculadora'
            }

sonny = {'Nombre':'Sonny Santino',
            'Apellido':'Corleone',
            'Puesto':'capo',
            'Físico':'pelo rizado',
            'Actor':'Mario Puzo',
            'Lugar de nacimiento':'Nueva York',
            'Sexo':'hombre',
            'Personalidad':'temperamental'
            }

tom = {'Nombre':'Tom Hagen',
            'Apellido': 'Hagen',
            'Puesto':'abogado',
            'Físico':'pelo rubio',
            'Actor':'Robert Duvall',
            'Lugar de nacimiento':'Irlanda/Estados Unidos',
            'Sexo':'hombre',
            'Personalidad':'racional'
            }

salvatore = {'Nombre':'Salvatore Tessio',
            'Apellido': 'Tessio',
            'Puesto':'dueño de un club',
            'Físico':'calvicie',
            'Actor':'Abe Vigoda',
            'Lugar de nacimiento':'Sicilia',
            'Sexo':'hombre',
            'Personalidad':'inteligente'}

luca_brasi = {'Nombre':'Luca Brasi',
            'Apellido': 'Brasi',
            'Puesto':'guardaespaldas',
            'Físico':'corpulento',
            'Actor':'Lenny Montana',
            'Lugar de nacimiento':'Rhode Island',
            'Sexo':'hombre',
            'Personalidad':'discreta'}

johnny_fontane = {'Nombre':'Johnny Fontane',
            'Apellido': 'Fontane',
            'Puesto':'cantante',
            'Físico':'entradas en el pelo pronunciadas',
            'Actor':'Al Martino',
            'Lugar de nacimiento':'Nueva York',
            'Sexo':'hombre',
            'Personalidad':'impulsiva'}

fredo = {'Nombre':'Fredo Federico',
            'Apellido':'Corleone',
            'Puesto':'capo',
            'Físico':'bigotito',
            'Actor':'John Cazale',
            'Lugar de nacimiento':'Nueva York',
            'Sexo':'hombre',
            'Personalidad':'traicionera'}

#**Lista personajes

personajes_lord = [Aragorn, Legolas, Gimli, Gollum, Sam, Frodo,Gandalf, Saruman, Galadriel, Boromir, orcos]

personajes_got = [jamie_lannister, tyrion_lannister, cersei_lannister, aria_stark, sansa_stark, bran_stark, john_snow, joffrey_baratheon, khal_drogo, daenerys_targaryen, caminantes_blancos]

personajes_simpson = [homero_simpson, bart_simpson, lisa_simpson, marge_simpson, maggie_simpson, señor_burns, nelson_muntz, moe_syzslak, milhouse_vanhouten, ned_flanders]

personajes_elpadrino = [vito, michael, sonny, tom, salvatore, luca_brasi, johnny_fontane, fredo]



personaje_escogido_a = personajes_simpson[random.randint(0,9)]

personaje_escogido_b = personajes_got[random.randint(0,10)]

personaje_escogido_c = personajes_elpadrino[random.randint(0,7)]

personaje_escogido_d = personajes_lord[random.randint(0,10)]



personaje_escogido_a['Nombre'].lower()

personaje_escogido_b['Nombre'].lower()

personaje_escogido_c['Nombre'].lower()

personaje_escogido_d['Nombre'].lower()


def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.06)
        else:
            time.sleep(0.5)

os.system("cls")

#**Empieza juego

title = pyfiglet.figlet_format("Adivina quien ?","ogre")
print(title)

message = '\033[4m'+'Instrucciones:\n'+ '\033[0;m'
typewriter(message)



print(" 1. Selecciona si quieres jugar a adivinar algún personaje de una serie o película. \n\n ¿Estás list@? En el siguiente menú aparecerá una lista de atributos del personaje.\n\n 2. Selecciona uno para recibir la primera pista. Piensa y elige con calma, solo podrás recibir 4 pistas!! \n 3. Si ya sabes de qué personaje se trata, puedes adivinar antes de recibir las 4 pistas, escribe Adivinar. \n 4. Ya tienes 4 pistas, es momento de adivinar!! \n")



print("Ps: puedes salirte del juego si escribes Quit")


message = "\n Comencemos ... \n "
typewriter(message)


message = "- Los Simpsons \n - Game of thrones \n - El padrino \n - The Lord of the rings \n"
typewriter(message)

#seleccion = input("Elige la peli o serie para adivinar el personaje:  ")
  
#seleccion = str(seleccion)


def preguntar_serie_peli():
    seleccion = input("\nElige la peli o serie para adivinar el personaje:  ")
    seleccion = str(seleccion)
    if seleccion.lower() == ('los simpsons') or seleccion.lower() == ('simpsons') or seleccion.lower() == ('simpson'):
        return seleccion
    elif seleccion.lower() == ('game of thrones') or seleccion.lower() == ('got'):
        return seleccion
    elif seleccion.lower() == ('lord of the rings') or seleccion.lower() == ('lotr') or seleccion.lower() == ('the lord of the rings') or seleccion.lower() == ('lord'):
        return seleccion
    elif seleccion.lower() == ('el padrino') or seleccion.lower() == ('padrino'):
        return seleccion
    else:
        print('\033[0;31m'+ 'Tu respuesta no es válida, intenta de nuevo. ' + '\033[0;m')
    return preguntar_serie_peli()


seleccion = preguntar_serie_peli()


inputusuario = ''
estatus = ''
preguntausuarioCount = 0

#**Adivina quien simpson desglosado
if seleccion.lower() == 'los simpsons' or seleccion.lower() == ('simpsons') or seleccion.lower() == ('simpson'):
    
    while inputusuario != 'Quit' and estatus != 'Game Over':     
        inputusuario = input("\n Escribe una de las siguientes caracteristicas para descubrir tu personaje: \n -Sexo \n -Edad \n -Pelo \n -Ropa \n -Energía \n -Gustos \n -Frase \n *Quiero adivinar!! \n\n  ")
    
        if preguntausuarioCount <= 3:
            if inputusuario.lower() == 'sexo' or inputusuario.lower() == ('sex'):
                print('\033[0;32m'+ personaje_escogido_a['Sexo']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'edad':
                print('\033[0;32m'+ personaje_escogido_a['Edad']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'pelo'or inputusuario.lower() == ('cabello'):
                print('\033[0;32m'+ personaje_escogido_a['Pelo']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'ropa':
                print('\033[0;32m'+ personaje_escogido_a['Ropa']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'energía' or inputusuario.lower() == 'energia':
                print('\033[0;32m'+ personaje_escogido_a['Energía'] +'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'gustos' or inputusuario.lower() == 'gusto':
                print('\033[0;32m'+ personaje_escogido_a['Gustos']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'frase' or inputusuario.lower() == ('frases'):
                print('\033[0;32m'+ personaje_escogido_a['Frase']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'quit':
                estatus ='Game Over'
                seeya = pyfiglet.figlet_format("Hasta la proxima...","rectangles")
                print(seeya)

            elif inputusuario.lower() == 'adivinar' or inputusuario.lower() == 'adivina' or inputusuario.lower() == 'quiero adivinar':
                resultadousuario = input("Debes adivinar el nombre del personaje:  ")
                if resultadousuario.lower() in personaje_escogido_a['Nombre'].lower():
                    estatus = 'Game Over'
                    winner = pyfiglet.figlet_format("Adivinaste!")
                    print(winner)
                else:
                    estatus = 'Game Over'
                    looser = pyfiglet.figlet_format("Game Over...\n No adivinaste","doom")
                    print(looser)

            else:
                print('\033[0;31m'+ 'Tu respuesta no es válida, intenta de nuevo. ' + '\033[0;m')

        else:
            resultadousuario = input("Ya no puedes tener más pistas. Debes adivinar el nombre del personaje:  ")
            if resultadousuario.lower() in personaje_escogido_a['Nombre'].lower():
                estatus = 'Game Over'
                winner = pyfiglet.figlet_format("Adivinaste!")
                print(winner)
               
            else:
                estatus = 'Game Over'
                looser = pyfiglet.figlet_format("Game Over...\n No adivinaste","doom")
                print(looser)
                

    pass

#**Adivina quien got desglosado

if seleccion.lower() == 'game of thrones' or seleccion.lower() == ('got'):   
    while inputusuario != 'Quit' and estatus != 'Game Over':     
        inputusuario = input("Escribe una de las siguientes caracteristicas para descubrir tu personaje: \n -Genero \n -Edad \n -Casa \n -Color de cabello \n -Estatura \n -Sobrevivio al final de la serie \n -Con que letra empieza su nombre \n *Quiero adivinar!! \n\n   ")
       
        if preguntausuarioCount <= 3:
            if inputusuario.lower() == 'genero' or inputusuario.lower() == 'género':
                print('\033[0;32m'+ personaje_escogido_b['Género']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'edad':
                print('\033[0;32m'+personaje_escogido_b['Edad']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'casa' or inputusuario.lower() == 'caza':
                print('\033[0;32m'+ personaje_escogido_b['Casa']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'estatura' or inputusuario.lower() == 'altura':
                print('\033[0;32m'+ personaje_escogido_b['Estatura']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'con que letra empieza su nombre' or inputusuario.lower() == 'letra':
                print('\033[0;32m'+ personaje_escogido_b['Con que letra empieza su nombre']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'sobrevivio al final de la serie' or inputusuario.lower() == 'sobrevivio':
                print('\033[0;32m'+ personaje_escogido_b['Sobrevivio al final de la serie']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'Color de cabello' or inputusuario.lower() == 'cabello' or inputusuario.lower() == 'pelo':
                print('\033[0;32m'+ personaje_escogido_b['Color de cabello']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'quit':
                estatus ='Game Over'
                seeya = pyfiglet.figlet_format("Hasta la proxima...","rectangles")
                print(seeya)

            elif inputusuario.lower() == 'adivinar' or inputusuario.lower() == 'adivina' or inputusuario.lower() == 'quiero adivinar':
                resultadousuario = input("Debes adivinar el nombre del personaje:  ")
                if resultadousuario.lower() in personaje_escogido_b['Nombre'].lower():
                    estatus = 'Game Over'
                    winner = pyfiglet.figlet_format("Adivinaste!")
                    print(winner)
                else:
                    estatus = 'Game Over'
                    looser = pyfiglet.figlet_format("Game Over...\n No adivinaste","doom")
                    print(looser)

            else:
                print('\033[0;31m'+ 'Tu respuesta no es válida, intenta de nuevo. ' + '\033[0;m')

        else:
            resultadousuario = input("Ya no puedes tener más pistas. Debes adivinar el nombre del personaje:  ")
            if resultadousuario.lower() in personaje_escogido_b['Nombre'].lower():
                estatus = 'Game Over'
                winner = pyfiglet.figlet_format("Adivinaste!")
                print(winner)
            else:
                estatus = 'Game Over'
                looser = pyfiglet.figlet_format("Game Over...\n No adivinaste","doom")
                print(looser)

    pass

#**Adivina quien padrino desglosado
if seleccion.lower() == 'el padrino' or seleccion.lower() == ('padrino'):  
    while inputusuario != 'Quit' and estatus != 'Game Over':     
        inputusuario = input("\n Escribe una de las siguientes caracteristicas para descubrir tu personaje: \n -Apellido \n -Puesto \n -Físico \n -Actor \n -Lugar de nacimiento \n -Sexo \n -Personalidad \n *Quiero adivinar!! \n\n  ")
    
        if preguntausuarioCount <= 3:
            if inputusuario.lower() == 'apellido' or inputusuario.lower() == ('apelido'):
                print('\033[0;32m'+ personaje_escogido_c['Apellido']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'puesto':
                print('\033[0;32m'+ personaje_escogido_c['Puesto']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'físico' or inputusuario.lower() == ('fisico'):
                print('\033[0;32m'+ personaje_escogido_c['Físico']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'actor':
                print('\033[0;32m'+ personaje_escogido_c['Actor']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'lugar de nacimiento' or inputusuario.lower() == 'lugar' or inputusuario.lower() == 'nacimiento':
                print('\033[0;32m'+ personaje_escogido_c['Lugar de nacimiento'] +'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'sexo':
                print('\033[0;32m'+ personaje_escogido_c['Sexo']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'personalidad':
                print('\033[0;32m'+ personaje_escogido_c['Personalidad']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'quit':
                estatus ='Game Over'
                seeya = pyfiglet.figlet_format("Hasta la proxima...","rectangles")
                print(seeya)

            elif inputusuario.lower() == 'adivinar' or inputusuario.lower() == 'adivina' or inputusuario.lower() == 'quiero adivinar':
                resultadousuario = input("Debes adivinar el nombre del personaje:  ")
                if resultadousuario.lower() in personaje_escogido_c['Nombre'].lower():
                    estatus = 'Game Over'
                    winner = pyfiglet.figlet_format("Adivinaste!")
                    print(winner)
                else:
                    estatus = 'Game Over'
                    looser = pyfiglet.figlet_format("Game Over...\n No adivinaste","doom")
                    print(looser)

            else:
                print('\033[0;31m'+ 'Tu respuesta no es válida, intenta de nuevo. ' + '\033[0;m')

        else:
            resultadousuario = input("Ya no puedes tener más pistas. Debes adivinar el nombre del personaje:  ")
            if resultadousuario.lower() in personaje_escogido_a['Nombre'].lower():
                estatus = 'Game Over'
                winner = pyfiglet.figlet_format("Adivinaste!")
                print(winner)
               
            else:
                estatus = 'Game Over'
                looser = pyfiglet.figlet_format("Game Over...\n No adivinaste","doom")
                print(looser)
                

    pass

#**Adivina quien lotr desglosado

if seleccion.lower() == 'lord of the rings'or seleccion.lower() == ('the lord of the rings') or seleccion.lower() == ('lord') or seleccion.lower() == ('lotr') :
    while inputusuario != 'Quit' and estatus != 'Game Over':     
        inputusuario = input("Escribe una de las siguientes caracteristicas para descubrir tu personaje: \n -Genero \n -Edad \n -Reino \n -Color de cabello \n -Estatura \n -Arma favorita \n -Con que letra empieza su nombre \n -Raza \n *Quiero adivinar!! \n\n  ")
   
        if preguntausuarioCount <= 3:
            if inputusuario.lower() == 'genero' or inputusuario.lower() == 'género':
                print('\033[0;32m'+ personaje_escogido_d['Género']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'edad':
                print('\033[0;32m'+ personaje_escogido_d['Edad']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'reino' or inputusuario.lower() == 'reyno' or inputusuario.lower() == 'rey':
                print('\033[0;32m'+ personaje_escogido_d['Reyno']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'estatura' or inputusuario.lower() == 'altura':
                print('\033[0;32m'+ personaje_escogido_d['Estatura']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'con que letra empieza su nombre' or inputusuario.lower() == 'letra':
                print('\033[0;32m'+ personaje_escogido_d['Con que letra empieza su nombre']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'arma favorita' or inputusuario.lower() == 'arma':
                print('\033[0;32m'+ personaje_escogido_d['Arma favorita']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'Color de cabello' or inputusuario.lower() == 'pelo':
                print('\033[0;32m'+ personaje_escogido_d['Color de cabello']+'\033[0;m')
                preguntausuarioCount += 1
            
            elif inputusuario.lower() == 'raza' or inputusuario.lower() == 'rasa':
                print('\033[0;32m'+ personaje_escogido_d['Raza']+'\033[0;m')
                preguntausuarioCount += 1

            elif inputusuario.lower() == 'quit':
                estatus ='Game Over'
                seeya = pyfiglet.figlet_format("Hasta la proxima...","rectangles")
                print(seeya)

            elif inputusuario.lower() == 'adivinar' or inputusuario.lower() == 'adivina' or inputusuario.lower() == 'quiero adivinar':
                resultadousuario = input("Debes adivinar el nombre del personaje:  ")
                if resultadousuario.lower() in personaje_escogido_d['Nombre'].lower():
                    estatus = 'Game Over'
                    winner = pyfiglet.figlet_format("Adivinaste!")
                    print(winner)
                else:
                    estatus = 'Game Over'
                    looser = pyfiglet.figlet_format("Game Over...\n No adivinaste","doom")
                    print(looser)

            else:
                print('\033[0;31m'+ 'Tu respuesta no es válida, intenta de nuevo. ' + '\033[0;m')

        else:
            resultadousuario = input("Ya no puedes tener más pistas. Debes adivinar el nombre del personaje:  ")
            if resultadousuario.lower() in personaje_escogido_d['Nombre'].lower():
                estatus = 'Game Over'
                winner = pyfiglet.figlet_format("Adivinaste!")
                print(winner)
            else:
                estatus = 'Game Over'
                looser = pyfiglet.figlet_format("Game Over...\n No adivinaste","doom")
                print(looser)

    pass
