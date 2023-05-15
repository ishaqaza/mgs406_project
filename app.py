from flask import Flask, render_template, request
import gunicorn
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database
db = mysql.connector.connect(
    host='localhost',
    user='flask',
    password='ubuntu',
    database='Project'
)

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

        # Insert the reservation into the database
        cursor = db.cursor()
        insert_query = 'INSERT INTO Reservations (name, email, date, time, party_size) VALUES (%s, %s, %s, %s, %s)'
        values = (name, email, date, time, party_size)
        cursor.execute(insert_query, values)
        db.commit()
        cursor.close()

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

# Managers page
@app.route('/managers')
def managers():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Reservations')
    reservations = cursor.fetchall()
    cursor.close()
    return render_template('managers.html', reservations=reservations)

if __name__ == '__main__':
    from gunicorn.app.wsgiapp import run
    run()
