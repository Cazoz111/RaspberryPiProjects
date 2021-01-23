from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@app.route('/')
def index():

    return "welcome to cooper's rainbow app!"


@app.route('/red')
def red():
    name = "red"
    background = "#FF0000"

    return render_template('rainbow.html', name = name, background = background)

@app.route('/orange')
def orange():
    name = "orange"
    background = "#FF8C00"

    return render_template('rainbow.html', name = name, background = background)




@app.route('/yellow')
def yellow():
    name = "yellow"
    background = "#FFFF00"

    return render_template('rainbow.html', name = name, background = background)


@app.route('/green')
def green():
    name = "green"
    background = "#008000"

    return render_template('rainbow.html', name = name, background = background)


@app.route('/blue')
def blue():
    name = "blue"
    background = "#00008B"

    return render_template('rainbow.html', name = name, background = background)

@app.route('/indigo')
def indigo():
    name = "indigo"
    background = "#4B0082"

    return render_template('rainbow.html', name = name, background = background)

@app.route('/violet')
def violet():
    name = "voilet"
    background = "#4F2F4F"

    return render_template('rainbow.html', name = name, background = background)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


