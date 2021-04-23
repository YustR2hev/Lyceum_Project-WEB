import os

from flask import (Flask, flash, redirect, render_template, request,
                   session, url_for)
from micawber import bootstrap_basic
from micawber.cache import Cache as OEmbedCache
from playhouse.flask_utils import FlaskDB
from utils import main as chemical_calculation

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    next_url = request.args.get('next') or request.form.get('next')
    if request.method == 'POST' and request.form.get('password'):
        password = request.form.get('password')
        # TODO: If using a one-way hash, you would also hash the user-submitted
        # password and do the comparison on the hashed versions.
        if password == app.config['ADMIN_PASSWORD']:
            session['logged_in'] = True
            session.permanent = True  # Use cookie to store session.
            flash('You are now logged in.', 'success')
            return redirect(next_url or url_for('index'))
        else:
            flash('Incorrect password.', 'danger')
    return render_template('login.html', next_url=next_url)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form.get('formulae'):
        formulae = request.form.get('formulae')
        answer = chemical_calculation(formulae)
        return render_template('index.html', answer=answer)
    return render_template('index.html')


def main():
    # database.create_tables([Entry, FTSEntry], safe=True)
    app.run(debug=True)


if __name__ == '__main__':
    main()
