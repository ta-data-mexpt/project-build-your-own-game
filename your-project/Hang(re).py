import random
from random import randint

words = ["AESTHETIC","BURGEON","CONTRIVE","DELETERIOUS","ELUCIDATE","ENTRENCHED","GAINSAY","HERETIC","LIONIZE","MISCONSTRUE","NUANCE","PREVARICATE","RESCIND","UNDERMINE","APEX"]
words_dict={"AESTHETIC":"connected with beauty and art and the understanding of beautiful things","BURGEON":"to begin to grow or develop rapidly","CONTRIVE":"to manage to do something despite difficulties","DELETERIOUS":"harmful and damaging","ELUCIDATE":"​to make something clearer by explaining it more fully","ENTRENCHED":"to establish something very strongly so that it is very difficult to change","GAINSAY":"to say that something is not true; to disagree with or deny something","HERETIC":"a person who believes in or practises religious heresy","LIONIZE":"to treat somebody as a famous or important person","MISCONSTRUE":"to understand somebody’s words or actions wrongly","NUANCE":"a very slight difference in meaning, sound, colour or somebody’s feelings that is not usually very obvious","PREVARICATE":"to avoid giving a direct answer to a question in order to hide the truth","RESCIND":"to officially state that a law, contract, decision, etc. no longer has any legal force","UNDERMINE":"to make something, especially somebody’s confidence or authority, gradually weaker or less effective","APEX":"​the top or highest part of something"}
ramd = randint(0,15)
word = list(words[ramd]) #convierte la palabra elegida en lista y es guardada en palabra
numbers = ["1","2","3","4","5","6","7","8","9"]
wordsc= words[ramd]
repeat= []
same = []
guess = []
mistakes=0
goods=0

for x in word:
    guess.append("_") #según el número de letras de la palabra se agrega un "_"
    same.append("-") #genera en la lista "igual" según el número de letras que tenga "palabra"

play = True

while play:

    #loop del juego
    print("\n ************************************************************************************** \n The meaning of the word that we are looking for is:\n","\n", words_dict[wordsc],"\n")
    print(guess, "Mistakes: " + str(mistakes), "Remaining tries: " + str(7-mistakes),"\n")

    player = input("Capture a letter: ").upper()

    if len(player) > 1:
        player = input("Capture a letter: ").upper() #si hay más de una letra se ejecuta este código

    for z in repeat:
        if player == z:
            player = input("Capture a different letter: ").upper() #busca si la letra está repetida en la lista "repetidas"

    if len(player) <1:
        player = input("Capture a letter: ").upper() #si no se ingresa nada se ejecuta este código

    for n in numbers:
        if player == n:
            player = input("Capture a letter: ").upper() #si hay un número en la entrada se ejecuta


    for x in word:

        if player == x:
            guess[word.index(x)] = player
            word[word.index(x)] = "-"
            repeat.append(player)

            if word == same:
                print("You win!")
                play = False

    if player not in wordsc:
        mistakes+=1

        if mistakes == 7:
            print("""\nYou lose, try again!

The word was: """+ wordsc)
            play = False

