#!/usr/bin/python3
''' script that starts a Flask web application '''

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ Function that close """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    ''' Function that return list of all states '''
    all_states = storage.all(State).values()
    return render_template('7-states_list.html', all_states=all_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
