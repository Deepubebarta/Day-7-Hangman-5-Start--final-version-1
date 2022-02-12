#Step 5

import random
import hangman_art
import hangman_words
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# end_of_game = False
# lives = 6
print(hangman_art.logo)
word = random.choice(hangman_words.word_list)
dashes = []
for i in word:
    dashes.append("_")

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
final_word = ''.join(dashes)
print(final_word)
total_chances = 6
status = 0
stage = 0
input_letter = []
hangman_art.stages.reverse()
print(f"Total chances are {total_chances}")
while total_chances > 0:
    tmp = ''.join(dashes)
    letter = input("Guess a letter\n").lower()
    if letter in input_letter:
        print("You have already eneter the same letter " + letter)
        print(hangman_art.stages[input_letter.index(letter)+1])
    else:
        input_letter.append(letter)
        for i in range(0, len(word)):
            if word[i] == letter:
                dashes[i] = letter

        total_chances -= 1
        final_word = ''.join(dashes)
        print(final_word)
        if tmp == final_word:
            stage +=1
            if stage == len(hangman_art.stages):
                print("You loose")
                continue
            else:
                print("Wrong guess")
                print(hangman_art.stages[stage])
                print(f"Total chances are {total_chances}")
        else:
            print("Your guess was correct, but need more guesses")
            print(f"Total chances are {total_chances}")
    

final_word = ''.join(dashes)
if final_word != word:
    print("The choosen word is: " + word)
for i in final_word:
    if i == "_":
        print("You loose")
        status = 1
        break

if status == 0:
    print("You won")
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     #Check if user is wrong.
#     if guess not in chosen_word:
#         #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")

#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")

#     #TODO-2: - Import the stages from hangman_art.py and make this error go away.
#     print(stages[lives])
