from flask import render_template, request
from app import app
from modules.event_list import add_new_event, events
from modules.event import *


@app.route('/')
def index():
    return render_template("index.html", title="Home", events=events)

@app.route('/add-event', methods=["POST"])
def add_event():
    return "Yipeee"
    # print(request.form)
    # event_title = request.form['title']
    # event_desc = request.form['description']
    # new_event = Event(event_title, event_desc)
    # add_new_event(new_event)
    # return render_template('index.html', title="Home", events=events)