#hangman test

wordtoguess = list("apple")

hashed_word = ""
guess_a_letter = "p"
x = 0
x2=x
letter_2_guess = raw_input("Guess a letter: ")
x = wordtoguess.count(letter_2_guess)
print "That letter was found: " + str(x) + " times!"
p = 0

while hashed_word != wordtoguess:
    for f in wordtoguess:
        if f == letter_2_guess:
            hashed_word = "y" * 5
            print hashed_word
        else:
            hashed_word = hashed_word + "x"
    letter_2_guess = raw_input("Guess a letter: ")
