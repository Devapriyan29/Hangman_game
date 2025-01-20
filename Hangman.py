from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of words for the game
#words = ['hangman', 'python', 'flask', 'game', 'web']
tot = ["Animal", "Bird", "Insect","Fruits","vegetables"]
types = [["tiger", "lion", "dog", "horse"], ["crow", "owl", "dove", "emu"], ["ant", "spider", "dragonfly", "fly"],["orange","mango","kiwi","apple","banana"],["potato","carrot","beans","tomato","chilli"]]
# Game state variables (stored temporarily in memory)
base=random.choice(tot)
pos=tot.index(base)
current_word = random.choice(types[pos])
guessed_letters = set()
attempts_left = 5

@app.route('/', methods=['GET', 'POST'])
def hangman():
    global current_word, guessed_letters, attempts_left,pos,base,tot,types

    # Create the display word (e.g., "_ a _ g _ a _")


    if request.method == 'POST':
        guess = request.form['guess'].lower()  # Get the guessed letter

        if guess not in guessed_letters:  # Add the new guess
            guessed_letters.add(guess)
            if guess not in current_word:
                attempts_left -= 1  # Reduce attempts for incorrect guesses
    display_word = ' '.join([char if char in guessed_letters else '_' for char in current_word])

        # Check game end conditions
    if '_' not in display_word:  # Win condition
        result = f'You won! The word was "{current_word}"🎉.'
        reset_game()
        return render_template('result.html', result=result)
    elif attempts_left == 0:  # Lose condition
        result = (f'You lost! '
                  f'The word was "{current_word}"☹. ️')
        reset_game()
        return render_template('result.html', result=result)

    # Render the game template with the current game state
    return render_template('index.html', display_word=display_word, attempts_left=attempts_left*'❤️',curr=base)


def reset_game():
    """Reset the game state for a new round."""
    global current_word, guessed_letters, attempts_left,pos,base,tot,types
    base = random.choice(tot)
    pos = tot.index(base)
    current_word = random.choice(types[pos])
    guessed_letters = set()
    attempts_left = 6


if __name__ == '__main__':
    app.run(debug=True)
