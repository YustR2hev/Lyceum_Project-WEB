from flask import (Flask, render_template, request)

from reaction_equation import main as chemical_calculation
from molar_mass import molarM as molar_mass_calculation
from substance_mass import  submass as substance_mass_calculation

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    return render_template('main-page.html')


@app.route('/reaction-equation', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form.get('formula'):
        formula = request.form.get('formula')
        answer = chemical_calculation(formula)
        return render_template('react-equation.html', answer=answer)
    return render_template('react-equation.html')


@app.route('/molar-mass', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST' and request.form.get('formula'):
        formula = request.form.get('formula')
        answer = molar_mass_calculation(formula)
        return render_template('molar-mass.html', answer=answer)
    return render_template('molar-mass.html')


@app.route('/substance-mass', methods=['GET', 'POST'])
def index3():
    if request.method == 'POST' and request.form.get('formula'):
        formula = request.form.get('formula')
        answer = substance_mass_calculation(formula)
        return render_template('substance-mass.html', answer=answer)
    return render_template('substance-mass.html')


def main():
    # database.create_tables([Entry, FTSEntry], safe=True)
    app.run(debug=False)


if __name__ == '__main__':
    main()
