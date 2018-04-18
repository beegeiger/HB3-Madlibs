"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    # return "Hi! This is the home page. "
    return """
    <html></html>
    """


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """ Ask the user if want to play game"""
    
    play_game = request.args.get("game_yesno")
    # no_play = request.args.get("No_Game")
    print play_game

    if play_game == "yes":
        return render_template("game.html")

    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Takes madlib inputs and puts them into the story"""

    person1 = request.args.get("person1")
    adjective = request.args.get("Adjective")
    verb1 = request.args.get("verb1")
    part_body = request.args.get("Body Part")
    number = request.args.get("Number")
    noun = request.args.get("Noun")
    adverb = request.args.get("Adverb")
    verb2 = request.args.get("Verb2")
    pronoun = request.args.get("Pronoun")
    person2 = request.args.get("Person2")

    return render_template("gameresults.html", name1=person1, description=adjective,
        action1=verb1, bodypart=part_body, num=number, thing=noun, adv=adverb, action2=verb2, 
        pro=pronoun, name2=person2)


#######################################################################

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
