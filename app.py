from flask import Flask, request, render_template, redirect
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickensarecool28748"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
stories=[{"code": "template1", "title": "Once upon"}, {"code": "template2", "title": "traveling"}]


@app.route('/form')
def show_form():
    return render_template("form.html", stories=stories)


@app.route('/story')
def get_greeting():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    story = request.args["story"]
    message=""
    if story == "template1":
        message = 'Once upon a time in a long-ago {place}, there lived a {adjective} {noun}. It love to {verb} {plural_noun}'.format(place=place, noun=noun, verb=verb,
    adjective=adjective, plural_noun=plural_noun)
    elif story == "template2":
        message = 'Yesterday I traveled to {place}, where I met {adjective} {noun}. He was going to {verb} {plural_noun}'.format(place=place, noun=noun, verb=verb,
    adjective=adjective, plural_noun=plural_noun)
    return render_template("story.html", message=message)



