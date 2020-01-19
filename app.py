from flask import Flask, render_template, request, jsonify
import json
import sqlite3
import nexmo
client = nexmo.Client(key='b10b01c2', secret='aopTYjkDBfn5vdRC')

import random as r

app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

@app.route('/sft')
def hello():
    return render_template('index.html')

@app.route("/search", methods=['POST'])  
def view():  
    source = request.form['source']
    destination = request.form['destination']
    query = "select * from users where source='"+source+"' and destination = '"+destination+"'"
    print(query)
    # return 'Hello'
    con = sqlite3.connect("users.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute(query)  
    rows = cur.fetchall()  
    return render_template("users.html",rows = rows)   

@app.route('/sft2')
def hello1():
    return render_template('index2.html')

@app.route("/searc", methods=['POST'])  
def view1():  
    pickup = request.form['pickup']
    dropp = request.form['drop']
    query = "select * from users1 where pickup='"+pickup+"' and dropp = '"+dropp+"'"
    print(query)
    # return 'Hello'
    con = sqlite3.connect("users.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute(query)  
    rows = cur.fetchall()  
    return render_template("users1.html",rows = rows)  

@app.route('/pay')
def hello4():
    return render_template('pay.html')

@app.route("/payment", methods=['POST'])  
def view4():  
    destination = request.form['destination']
    modeoftransport = request.form['modeoftransport']
    email = request.form['email']
    source = request.form['source']
    query = "select * from users where modeoftransport = '"+modeoftransport+"' and destination = '"+destination+"'"
    print(query)
    # return 'Hello'
    con = sqlite3.connect("users.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute(query)  
    rows = cur.fetchall()  
    return render_template("pays.html",rows = rows)  


@app.route('/payna')
def pay2():
    return render_template('pay_na.html')

@app.route("/payn", methods=['POST'])  
def pay1():  
    email = request.form['email']
    query = "select * from payments_n where payment_status = 'paid' and email = '"+email+"'"
    print(query)
    # return 'Hello'
    con = sqlite3.connect("payments.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute(query)  
    rows = cur.fetchall()  
    return render_template("pay_n.html",rows = rows)  

@app.route('/local')
def hello9():
    return render_template('local.html')


@app.route("/local_pay", methods=['POST'])  
def view9():  
    email = request.form['email']
    query = "select * from payments_local where payment_status = 'paid' and email = '"+email+"'"
    print(query)
    # return 'Hello'
    con = sqlite3.connect("payments.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute(query)  
    rows = cur.fetchall()  
    return render_template("local1.html",rows = rows)   

@app.route('/')
def login():
    return render_template('login.html')

@app.route("/validate", methods=['POST'])  
def view8():  
    username = request.form['username']
    password = request.form['password']
    query = "select * from login where username='"+username+"' and password = '"+password+"'"
    print(query)
    # return 'Hello'
    con = sqlite3.connect("payments.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute(query)  
    rows = cur.fetchall()  
    return render_template("home.html",rows=rows)   
def otpgen():
    otp=""
    for i in range(4):
        otp+=str(r.randint(1,9))
    print ("Your One Time Password is ")
    print (otp)
otpgen()

@app.route('/booknow')
def booknow():
    return render_template('booknow.html')

@app.route("/book", methods=['POST'])  
def view10():  
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    source = request.form['source']
    destination = request.form['destination']
    modeoftransport = request.form['modeoftransport']
    phnumber = request.form['phnumber']
    client.send_message({'from': 'Nexmo','to': '919666697782','text': 'Hello, Your ticket to '+destination+' is waiting for payment, Thank You Regards-EasyTravel',})
    tickets_required = request.form['noofseats']
    con = sqlite3.connect("payments.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("insert into bookings_for_national values ('"+fname+"','"+lname+"','"+email+"','"+phnumber+"','"+source+"','"+destination+"','"+modeoftransport+"','"+tickets_required+"')")  
    cur.execute("select * from bookings_for_national where email = '"+email+"'")
    rows = cur.fetchall()  
    return render_template("bat.html",rows = rows)   

@app.route('/mybook')
def booknow1():
    return render_template('mybook.html')

@app.route('/home1', methods=['POST'])
def home1():
    return render_template('home.html')


@app.route('/book_international')
def booknow2():
    return render_template('international.html')

@app.route("/list_international", methods=['POST'])  
def view24():
    source = request.form['source']
    destination = request.form['destination']
    con = sqlite3.connect("payments.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    #cur.execute("insert into bookings_for_national values ('"+fname+"','"+lname+"','"+email+"','"+phnumber+"','"+source+"','"+destination+"','"+modeoftransport+"','"+tickets_required+"')")  
    cur.execute("select * from list_for_international where destination = '"+destination+"'")
    rows = cur.fetchall()  
    return render_template("table.html",rows = rows)   

app.run(port=9000)
