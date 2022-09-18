#we import the modules that we are going to use in the development
import random
import os
#we define the function run
def run():
    
#create a list with all the hangman pics
    IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#we define all the variables and create 2 list
    DB = ["C","JAVA","PHP","JAVASCRIPT","PYTHON",]#list with words
    word = random.choice(DB)
    spaces=["_"] * len(word)#list with spaces*word len
    attemps = 6
    play="si"#flag variable
    
    


    while play=="si":
        os.system("cls")
        for character in spaces:
            print(character,end=" ")
        print(IMAGES[attemps])
        letter=input("Elije una letra: ").upper()#player answer
        found = False
        for idx,character in enumerate(word):
            if character == letter:#fill spaces with letters
                spaces[idx]= letter
                found = True
        
        if not found:#if letters are wrong -1 attemps
            attemps -= 1

        if "_" not in spaces:#player wins
            os.system("cls")
            score =round(len(word)*attemps)#if you do not make mistakes in the letters your score will be higher
            print("Ganaste")
            print("Tienes ",score," puntos,felicidades")
            play=input("quieres jugar otra vez (si) o (no) ?")#we update flag variable
            word = random.choice(DB)#restart word
            spaces=["_"] * len(word)#restar spaces 
            attemps = 6#restart attemps
        
        if attemps == 0:#player loses
            os.system("cls")
            print("Perdiste")
            play=input("Quieres jugar otra vez (si) o (no)?")#we update flag variable
            word = random.choice(DB)#restart word
            spaces=["_"] * len(word)#restar spaces 
            attemps = 6#restart attemps
        
        if play == 'no':#the loop will break 
            break            

if __name__ == '__main__':
    run()
