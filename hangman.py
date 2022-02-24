from replit import clear
import random
from stages import stages

lives = 6
word_list = ['lamborghini', 'bugatti', 'mac_laren', 'honda', 'toyota', 'dodge', 'chevrolet', 'mustang', 'benz',
             'aston marti']
print('this is hangman for cars, get prepared')
chosen_word = random.choice(word_list)

display = []
for position in range(len(chosen_word)):
    display.append('_')

while True:
    clear()
    guess = input('guess a letter: ')

    clear()

    if guess in display:
        print(f"you have already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f'the letter you guesses {guess}, is not in the chosen words.')
        lives -= 1

        print(stages[lives])

        if lives == 0:
            print('you lose')
            break
    print(f"{' '.join(display)}")
    if not '_' in display:
        print('you won')
        break
