import random

# words = ["WINDOWS","UMBRELLA","MACHINE","COMPUTER", "SCIENCE"]

f = open("words.txt", "r")
data = f.readline()
words = data.split()
word = random.choice(words)
word = word.upper()

total_chances = 10
guessed_word = "-"*len(word)

while total_chances != 0:
    print(guessed_word)
    letter = input("Guess a letter: ").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]
        if guessed_word == word:
            print("congratulations you won!!")

    else:
        total_chances -= 1
        print("Incorrect guess")
        print("the rem chanches are: ", total_chances)

else:
    print("Game over")
    print("you lose")
    print("all the chances are overr")
    print("the correct word is: ",word)

