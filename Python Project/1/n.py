from m import app
from flask import Flask, redirect, url_for, request,flash,render_template
@app.route('/type_ho/<usern>')
def type_ho(usern):
    return render_template('type.html',usern = usern,flag = 1)
@app.route('/data/<usern>/<value>',methods =['POST'])
def typeo(usern,value):
    type_w= request.form["Amount_w"]
    type_p= request.form["Amount_p"]
    type_s= request.form["Amount_s"]
    if( type_w == '' and type_p == '' and type_s!=''):
        flagb = 1.5
        amount = type_s
    elif( type_w != '' and type_p == '' and type_s ==''):
        flagb = 3
        amount = type_w
    elif( type_w == '' and type_p != '' and type_s ==''):
        flagb = 2
        amount = type_p
    elif(type_w != '' and (type_p !='' or type_s != '')):
        flag = 2
        return render_template('type.html',usern = usern,value = value,flag = flag)
    elif(type_p != '' and (type_w !='' or type_s != '')):
        flag = 2
        return render_template('type.html',usern = usern,value = value,flag = flag)
    elif(type_s != '' and (type_p !='' or type_w != '')):
        flag = 2
        return render_template('type.html',usern = usern,value = value,flag = flag)
    else:
        flag = 2
        return render_template('type.html',usern = usern,value = value,flag = flag)
    file = open("1.txt", "r")
    details = file.readlines()
    i = 0
    while(details[i] != 'end' + str('\n')):
        if details[i] == usern + str('\n'):
            i += 5
            if float(amount) > float(details[i]):
                flag = 3
                return render_template('type.html',usern = usern,value = value,flag = flag)
        i += 1
    file.close()
    return redirect(url_for('deduct',usern = usern,flagb = flagb,amount=amount,value = value))
