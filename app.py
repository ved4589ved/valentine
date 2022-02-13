
from pickle import TRUE
import sqlite3

from flask import Flask, render_template, request, session, redirect, url_for, g
# con = sqlite3.connect('student.db', check_same_thread=False)
# c = con.cursor()
# c.execute('''CREATE TABLE studentd (username text, name text, password text)''')
# c.execute('''CREATE TABLE prefrence (username text, onep text, twop text, threep text, fourp text)''')


app = Flask(__name__)
app.secret_key = "super secret key"

@app.route("/", methods=['GET','POST'])
def hello():
    r=''
    msg=''
    if request.method=='POST':
        username= request.form['usernames']
        password = request.form['password']
        con = sqlite3.connect('student.db', check_same_thread=False)
        c = con.cursor()
        c.execute("SELECT * FROM studentd WHERE username = '"+username+"' and password= '"+password+"'")
        r= c.fetchall()
        con.commit()
        con.close()
        for i in r:
            if username==i[0] and password==i[2]:
                session['logedin']=True
                session["username"]= username
                session['name']= i[1]
                
                return redirect(url_for('profile'))
                
            else:
                msg='username or password is not correct'
    # print(r[0])

    return render_template('login.html', y= msg)

@app.route("/register", methods=['GET','POST'])
def helloh():
    y=''
    if request.method=='POST':
        if request.form['usernamei']!= '' and request.form['passwordi']!='' and request.form['name']!='':
            usernamei= request.form['usernamei']
            password= request.form['passwordi']
            name = request.form['name']
            con = sqlite3.connect('student.db', check_same_thread=False)
            c = con.cursor()
            c.execute("SELECT * FROM studentd WHERE username = '"+usernamei+"'")
            if len(c.fetchall())==0:
                c.execute("INSERT INTO studentd VALUES('"+usernamei+"', '"+name+"', '"+password+"')")
                con.commit()
                con.close()

                return redirect(url_for('profile'))
            else:
                y='user exist please login'
                
            
        
            

        
    return render_template('register.html', msg=y)

@app.route("/profile", methods=['GET','POST'])
def profile():
    y=''
    try:
        if session['username']!='':
            if request.method=='POST':
                firstp= request.form['firstp']
                secondp = request.form['secondp']
                thirdp= request.form['thirdp']
                fourthp= request.form['fourthp']
                con = sqlite3.connect('student.db', check_same_thread=False)
                c = con.cursor()
                c.execute("SELECT * FROM prefrence WHERE username = '"+session['username']+"'")
                if len(c.fetchall())==0 and firstp!='' and secondp!='' and thirdp!='' and fourthp!='':
                    c.execute("INSERT INTO prefrence VALUES('"+session['username']+"', '"+firstp+"', '"+secondp+"', '"+thirdp+"', '"+fourthp+"')")
                    con.commit()
                    con.close()
                else:
                    y='either you have already filled or field is empty'
                


                
        
            return render_template('profile.html', msg=y)
    except KeyError:
        return render_template('login.html')
@app.route("/database", methods=['GET','POST'])
def hellohp():
    con = sqlite3.connect('student.db', check_same_thread=False)
    c = con.cursor()
    c.execute("SELECT * FROM studentd")
    y= c.fetchall()
    c.execute("SELECT * FROM prefrence")
    z= c.fetchall()

    return render_template('database.html', msg=y, msg2=z)
if __name__== "__main__":
    app.run(debug=True)

