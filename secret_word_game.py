import os
os.system('cls')

correct_letters = ''
attempts = 6
numbers = '1234567890'

while True:
    secret_word = input('type the secret word: ')
    if secret_word in numbers:
        print('Only letters!!')
        continue
    else:
        break

os.system('cls')

while True:
    digited_word = input('type a letter: ')

    if len(digited_word) > 1:
        print('type only one word')
        continue
    
    if digited_word in numbers:
        print('Only letters!!')
        continue
    
    if digited_word in secret_word:
        correct_letters += digited_word

    generated_word = ''

    for secret_letter in secret_word:
        if secret_letter in correct_letters:
            generated_word += secret_letter
        else:
            generated_word += '*'

    if digited_word in secret_word:
        print('Correct letter!!')
    else:
        print('Wrong letter')
        attempts -= 1
        print(f'Attempts left {attempts}')

    if attempts == 0:
        os.system('cls')
        print('You lost!!')
        break

    print(generated_word)

    if generated_word == secret_word:
        os.system('cls')
        print(f'You guessed the word, it was {secret_word}')
        break