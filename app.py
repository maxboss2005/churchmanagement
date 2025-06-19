from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object('config')

mysql = MySQL(app)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/members')
def members():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM members")
    data = cur.fetchall()
    cur.close()
    return render_template('members.html', members=data)

@app.route('/add', methods=['POST'])
def add_member():
    name = request.form['name']
    contact = request.form['contact']
    status = request.form['status']
    ministry = request.form['ministry']
    join_date = request.form['join_date']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO members (name, contact, status, ministry, join_date) VALUES (%s, %s, %s, %s, %s)",
                (name, contact, status, ministry, join_date))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('members'))

if __name__ == '__main__':
    app.run(debug=True)