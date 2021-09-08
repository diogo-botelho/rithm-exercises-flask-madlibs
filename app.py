from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)
    
@app.get("/")
def show_input_form():
    """Display a form to collect the inputs required to generate a madLib"""
    words = silly_story.prompts

    return render_template(
        "questions.html",
        words = words)

@app.get("/results")
def create_story():
    """Create MadLibs story based on user inputs"""
    answers = request.args
    story = silly_story.generate(answers)
    
    return render_template(
        "story.html",
        story = story)