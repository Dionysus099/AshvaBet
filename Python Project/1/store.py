from flask import Flask, redirect, url_for, request,render_template
from m import app
import os
@app.route('/signup',methods = ['POST'])
def signup():
    if(request.method =='POST'):
        usern = request.form['U_name']
        userp = request.form['U_pass']
        userag = request.form['U_age']
        usergen = request.form['U_gen']
        userdob = request.form['U_dob']
        if(usern == '' or userp == '' or userag == '' or usergen==''):
            return render_template("signup.html",flag1=2)
        file = open('1.txt','r')
        file2 = open('2.txt','a')
        lines = file.readlines()
        i = 0
        for j in lines:
            if(j == str(usern)+'\n'):
                return render_template("signup.html",flag1=1)
        while(lines[i]!= 'end\n'):
            file2.write(lines[i])
            i+=1
        file2.write('\n'+usern+'\n')
        file2.write(userp+'\n')
        file2.write(userag+'\n')
        file2.write(usergen+'\n')
        file2.write(userdob+'\n')
        file2.write('500\n')
        file2.write('end\n')
        os.remove('1.txt')
        os.rename('2.txt', '1.txt')
        return render_template("index.html",flag = 2, flage = 3)
      
