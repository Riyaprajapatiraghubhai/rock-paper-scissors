from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    user_choice = None
    computer_choice = None

    if request.method == 'POST':
        user_choice = request.form['choice']
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Paper' and computer_choice == 'Rock') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper'):
            result = 'You win!'
        else:
            result = 'You lose!'

    return render_template('index.html', result=result,
                           user_choice=user_choice,
                           computer_choice=computer_choice)

if __name__ == '__main__':
    app.run(debug=True)
