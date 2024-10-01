from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', current_page='home')


# @app.route('/about')
# def about():
#    return render_template('about.html', current_page='about')


@app.route('/enjhin')
def enjhin():
    return render_template('enjhin.html', current_page='enjhin')


@app.route('/fizziks-soft-body')
def fizziks_soft_body():
    return render_template('fizziks-soft-body.html',
                           current_page='fizziks-soft-body')


@app.route('/fizziks-rigid-body')
def fizziks_rigid_body():
    return render_template('fizziks-rigid-body.html',
                           current_page='fizziks-rigid-body')


@app.route('/cv')
def cv():
    return render_template('cv.html', current_page='cv')


if __name__ == '__main__':
    app.run(debug=True)
