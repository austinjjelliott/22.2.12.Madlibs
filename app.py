from flask import Flask, render_template, request
from stories import Story

app = Flask(__name__)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"], 
    """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        answers = {
            "place": request.form['place'],
            "noun": request.form['noun'],
            "verb": request.form['verb'],
            "adjective": request.form['adjective'],
            "plural_noun": request.form['plural_noun']
        }
        story_text = story.generate(answers)
        return render_template('results.html', story_text = story_text)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)