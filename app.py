from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import story_options


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def choose_madlibs_story():
    """Display a dropdown to choose a madlib story template"""

    return render_template("choose-story.html")
    
@app.get("/questions") 
def collect_madlibs_prompt():
    """Display a form to collect the inputs required to generate a madLib"""
    
    print("request.args ", request.args)
    selected_story = request.args["select-story"]
    story_instance = story_options[selected_story]

    prompts = story_instance.prompts

    return render_template(
        "questions.html",
        prompts = prompts)

# TO DO: Update below for dynamic story selection

@app.get("/results")
def create_story():
    """Create MadLibs story based on user inputs"""
    answers = request.args
    story = story_instance.generate(answers)
    
    return render_template(
        "story.html",
        story = story)