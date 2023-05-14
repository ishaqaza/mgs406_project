import mysql.connector
import gunicorn
from flask import Flask, render_template, request

app = Flask(__name__)

# Connect to the MySQL database
db = mysql.connector.connect(
    host='localhost',
    user='flask',
    password='ubuntu',
    database='Project'
)

# This is necessary for Gunicorn to work correctly
application = app

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Reservation page
@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        time = request.form['time']
        party_size = request.form['party-size']

        # Render the confirmation page with the name and date of the reservation
        return render_template('confirmation.html', name=name, date=date, time=time, party_size=party_size)

    return render_template('reservation.html')

# Menu page
@app.route('/menu')
def menu():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM menu')
    menu_items = cursor.fetchall()
    cursor.close()
    return render_template('menu.html', menu_items=menu_items)

if __name__ == '__main__':
    from gunicorn.app.wsgiapp import run
    run()
