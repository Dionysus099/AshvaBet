from flask import Flask, redirect, url_for, request,flash,render_template
from m import app
@app.route('/instructions/<usern>')
def instructions(usern):
    file = open("instructions.txt", "r")
    display = file.readlines()
    file.close()
    return render_template('instructions.html', title = 'instructions', display = display,usern = usern)