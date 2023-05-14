from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Connect to MySQL database
db = sql.connect(
    host="localhost",
    user="flask",
    password="ubuntu",
    database="Project"
)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Menu page
@app.route('/menu')
def menu():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM menu')
    menu_items = cursor.fetchall()
    cursor.close()
    return render_template('menu.html', menu=menu_items)

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

        # Connect to MySQL database
        db = sql.connect(
            host="localhost",
            user="flask",
            password="ubuntu",
            database="flask_db"
        )
        cursor = db.cursor()

        # Insert the reservation data into the database
        cursor.execute('''
            INSERT INTO reservations (name, email, date, time, party-size)
            VALUES (%s, %s, %s, %s, %s)
        ''', (name, email, date, time, party_size))
        db.commit()

        # Close the cursor and the database connection
        cursor.close()
        db.close()

        # Render the confirmation page with the name and date of the reservation
        return render_template('confirmation.html', name=name, date=date, email=email, party_size=party_size)

    return render_template('reservation.html')

if __name__ == '__main__':
    app.run(debug=True)
