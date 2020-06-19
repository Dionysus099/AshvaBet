from flask import Flask, redirect, url_for, request,flash,render_template
from m import app
flag = 0
from n import *
@app.route('/')
def new():
    return render_template("index.html",flag = 0)
@app.route('/login',methods = ['POST'])
def login():
    if(request.method) == 'POST':
        usern = request.form['U_Name']
        userp = request.form['U_Pass']
        file = open('1.txt','r')
        lines = file.readlines()
        i = 0
        while(lines[i]!='end\n'):
            if(lines[i] == str(usern)+'\n'):
                i+=1
                if(lines[i] == str(userp)+'\n'):
                    return redirect(url_for('home',usern=usern))
            i+=1
        return render_template("index.html",flag = 1)

@app.route('/s')
def s():
    return render_template("signup.html")