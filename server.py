from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '5f881a93f7d5c18c69af0795269d28e0759a92e967f2efcdfbf5cfee0f5dac9f'

@app.before_first_request
def initialize():
    session['visits'] = 0
    session['increment'] = 2

@app.route('/', methods=["GET"])
def index():
    session['visits'] += 1
    inc_btn = f"{session['increment']}"
    if session['visits'] == 1:
        txt = f"{session['visits']} time"
    else:
        txt = f"{session['visits']} times"
    return render_template("index.html", text=txt, inc=inc_btn)

@app.route('/destroy_session', methods=["GET", "POST"])
def reboot():
    session.clear()
    session['visits'] = 0
    session['increment'] = 2
    return redirect('/')

@app.route('/count', methods=["POST"])
def addCount():
    session['visits'] += (session['increment'] - 1)
    return redirect('/')

@app.route('/minus_one', methods=["POST"])
def minusOne():
    if session['increment'] <= 1:
        session['increment'] = 1
    else:
        session['increment'] -= 1
    session['visits'] -= 1
    return redirect('/')

@app.route('/plus_one', methods=["POST"])
def plusOne():
    session['increment'] += 1
    session['visits'] -= 1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)