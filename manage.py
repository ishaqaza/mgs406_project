from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/reservation')
def reservation():
    return render_template('reservation.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)
