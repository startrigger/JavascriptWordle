import random
short_words = ['known', 'knows', 'label', 'labor', 'links']
correct = random.choice(short_words)
strWrong = ""
print(
"""
      Welcome to Wordle!!!

      Guess the word based on clues provided.
      Upper case indicates correct letter in wrong place.
      * placeholder for correct letter.
      (press the enter key at prompt to quit)
"""
      )
guess = input("Your guess: ")
while guess != correct and guess != "":
    if guess == "crack":
        print(correct)
    print("Sorry, that's not it\n")
    intLetterPosition = 0
    strCurrent = ""
    for element in guess:
        if correct.find(element) > -1:
            if correct.find(element,intLetterPosition) == guess.find(element,intLetterPosition):
                if strCurrent.find(element.upper()) > -1:
                    strCurrent = strCurrent.replace(element.upper(),"*")
                strCurrent = strCurrent + element
            else:
                if strCurrent.find(element) < 0:
                    strCurrent = strCurrent + element.upper()
                else:
                    strCurrent = strCurrent + "*"
        else:
            strCurrent = strCurrent + "*"
            if strWrong.find(element) < 0:
                strWrong = strWrong + " " + element
        intLetterPosition = intLetterPosition + 1
    print("Wrong: " + strWrong)
    print("Guess status: " + strCurrent + "\n")
    guess = input("Your guess: ")
if guess == correct:
    print("That's it, you guessed it!\n")
print("Thanks for playing")
input("\n\nPress the enter key to exit")