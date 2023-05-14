from flask import Flask, render_template
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
@app.route('/reservation')
def reservation():
    return render_template('reservation.html')

# Confirmation page
@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

# Menu page
@app.route('/menu')
def menu():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM menu')
    menu_items = cursor.fetchall()
    cursor.close()
    return render_template('menu.html', menu_items=menu_items)

if __name__ == '__main__':
    app.run(debug=True)
