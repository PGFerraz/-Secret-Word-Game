# -Secret-Word-Game
A guessing game where the user tries to guess a secret word letter by letter.

This Python script implements a simple command-line guessing game where the player tries to guess a secret word one letter at a time. Here’s a breakdown of how the game works:

Setup: The player is prompted to input a secret word, which must consist only of letters (digits are not allowed). The game will continue to prompt until a valid word is entered.

Gameplay:

The player is given 6 attempts to guess the letters in the secret word.
For each guess, the player inputs a single letter.
The script provides feedback on whether the guessed letter is correct or not.
Correctly guessed letters are revealed in their respective positions within the word, while unguessed letters are shown as asterisks (*).
Win/Loss Conditions:

If the player correctly guesses all the letters in the secret word before running out of attempts, they win the game.
If the player uses up all 6 attempts without guessing the entire word, they lose the game.
User Interface:

The screen is cleared at various points to keep the interface clean and to show the updated state of the game.
This game provides a basic implementation of a word-guessing challenge and can be further extended with additional features or improved user experience.
