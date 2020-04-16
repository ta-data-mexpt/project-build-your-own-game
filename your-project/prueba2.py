import random
IMÁGENES_AHORCADO = ['''

  3.

  4.   +---+

  5.   |   |

  6.       |

  7.       |

  8.       |

  9.       |

 10. =========''', '''

 11.

 12.   +---+

 13.   |   |

 14.   O   |

 15.       |

 16.       |

 17.       |

 18. =========''', '''

 19.

 20.   +---+

 21.   |   |

 22.   O   |

 23.   |   |

 24.       |

 25.       |

 26. =========''', '''

 27.

 28.   +---+

 29.   |   |

 30.   O   |

 31.  /|   |

 32.       |

 33.       |

 34. =========''', '''

 35.

 36.   +---+

 37.   |   |

 38.   O   |

 39.  /|\  |

 40.       |

 41.       |

 42. =========''', '''

 43.

 44.   +---+

 45.   |   |

 46.   O   |

 47.  /|\  |

 48.  /    |

 49.       |

 50. =========''', '''

 51.

 52.   +---+

 53.   |   |

 54.   O   |

 55.  /|\  |

 56.  / \  |

 57.       |

 58. =========''']

 59. palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()

 60.

 61. def obtenerPalabraAlAzar(listaDePalabras):

 62.     # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.

 63.     índiceDePalabras = random.randint(0, len(listaDePalabras) - 1)

 64.     return listaDePalabras[índiceDePalabras]

 65.

 66. def mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):

 67.     print(IMÁGENES_AHORCADO[len(letrasIncorrectas)])

 68.     print()

 69.

 70.     print('Letras incorrectas:', end=' ')

 71.     for letra in letrasIncorrectas:

 72.         print(letra, end=' ')

 73.     print()

 74.

 75.     espaciosVacíos = '_' * len(palabraSecreta)

 76.

 77.     for i in range(len(palabraSecreta)): # completar los espacios vacíos con las letras adivinadas

 78.         if palabraSecreta[i] in letrasCorrectas:

 79.             espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]

 80.

 81.     for letra in espaciosVacíos: # mostrar la palabra secreta con espacios entre cada letra

 82.         print(letra, end=' ')

 83.     print()

 84.

 85. def obtenerIntento(letrasProbadas):

 86.     # Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.

 87.     while True:

 88.         print('Adivina una letra.')

 89.         intento = input()

 90.         intento = intento.lower()

 91.         if len(intento) != 1:

 92.             print('Por favor, introduce una letra.')

 93.         elif intento in letrasProbadas:

 94.             print('Ya has probado esa letra. Elige otra.')

 95.         elif intento not in 'abcdefghijklmnñopqrstuvwxyz':

 96.             print('Por favor ingresa una LETRA.')

 97.         else:

 98.             return intento

 99.

100. def jugarDeNuevo():

101.     # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.

102.     print('¿Quieres jugar de nuevo? (sí o no)')

103.     return input().lower().startswith('s')

104.

105.

106. print('A H O R C A D O')

107. letrasIncorrectas = ''

108. letrasCorrectas = ''

109. palabraSecreta = obtenerPalabraAlAzar(words)

110. juegoTerminado = False

111.

112. while True:

113.     mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)

114.

115.     # Permite al jugador escribir una letra.

116.     intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

117.

118.     if intento in palabraSecreta:

119.         letrasCorrectas = letrasCorrectas + intento

120.

121.         # Verifica si el jugador ha ganado.

122.         encontradoTodasLasLetras = True

123.         for i in range(len(palabraSecreta)):

124.             if palabraSecreta[i] not in letrasCorrectas:

125.                 encontradoTodasLasLetras = False

126.                 break

127.         if encontradoTodasLasLetras:

128.             print('¡Sí! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')

129.             juegoTerminado = True

130.     else:

131.         letrasIncorrectas = letrasIncorrectas + intento

132.

133.         # Comprobar si el jugador ha agotado sus intentos y ha perdido.

134.         if len(letrasIncorrectas) == len(IMÁGENES_AHORCADO) - 1:

135.             mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)

136.             print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')

137.             juegoTerminado = True

138.

139.     # Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).

140.     if juegoTerminado:

141.         if jugarDeNuevo():

142.             letrasIncorrectas = ''

143.             letrasCorrectas = ''

144.             juegoTerminado = False

145.             palabraSecreta = obtenerPalabraAlAzar(palabras)

146.         else:

147.             break
