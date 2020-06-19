from flask import Flask, render_template,redirect,url_for,request
from m import app
import os
@app.route('/wall/<usern>',methods=['POST'])
def add_w(usern):
    amount = request.form['amount']
    file = open("1.txt", "r")
    details = file.readlines()
    i = 0
    while(details[i] != 'end' + str('\n')):
        if details[i] == usern + str('\n'):
            i += 5
            details[i] = str(float(details[i]) + float(amount)) + str('\n')
            break
        i += 1
    file.close()
    file = open("2.txt", "a")
    for lines in details:
        file.write(lines)
    os.remove("1.txt")
    os.rename("2.txt", "1.txt")
    return redirect(url_for('profile',usern=usern))