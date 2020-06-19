from flask import Flask, render_template,redirect,url_for
from m import app
import random
import os
@app.route('/deduct/<amount>/<flagb>/<value>/<usern>')
def deduct(usern, amount,flagb,value):
    file = open("1.txt", "r")
    details = file.readlines()
    i = 0
    while(details[i] != 'end\n'):
        if (details[i] == usern +'\n') :
            i += 5
            details[i] = str(float(details[i]) - float(amount))+'\n'
            break
        i += 1
    file.close()
    file = open("2.txt", "a")
    for lines in details:
        file.write(lines)
    os.remove("1.txt")
    os.rename("2.txt", "1.txt")
    return redirect(url_for('com', usern = usern, flagb = flagb, amount=amount,value = value))
