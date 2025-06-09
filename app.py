from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = 'secret123'

db_work = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    raise_on_warnings=True
)
cursor_work = db_work.cursor()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cursor_work.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor_work.fetchone()
        
        if user:
            return "Login Successful! Welcome, " + username
        else:
            flash("Invalid username or password")
            return redirect(url_for('login'))
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
