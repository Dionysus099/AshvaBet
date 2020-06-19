from flask import Flask, redirect, url_for, request,flash,render_template
from m import app
import random
import time
@app.route('/com/<usern>/<flagb>/<value>/<amount>')
def com(usern,flagb,amount,value):
    def search(l,i):
        k=0
        while(k<10):
            if(i == l[k]):
                return k+1
            k+=1
    count = 0
    l = [1,2,3,4,5,6,7,8,9,10]
    comm = []
    random.shuffle(l)
    hero = int(value)
    while(count<8):
        rc = random.choice([1,2])
        pos = search(l,hero)
        x = pos
        if(rc== 1 and pos!=1 and pos!=10):
            movep = random.choice(range(1,pos))
            y = movep
            while(x != y):
                comm.append("No."+str(hero)+" crossed No."+str(l[x-2])+". No."+str(hero)+" moved to postion "+str(x-1))
                x-=1
            l.pop(pos-1)
            l.insert(movep-1,hero)
        elif(rc==2 and pos!=10 and pos!=1):
            movep = random.choice(range(pos+1,11))
            y = movep
            while(x!= y):
                comm.append("No."+str(l[x])+" crossed No."+str(hero)+". No."+str(hero)+" moved to postion " +str(x+1))
                x+=1
            l.pop(pos-1)
            l.insert(movep-1,hero)
        elif(pos == 1):
            movep = random.choice(range(2,5))
            while(x!=movep):
                comm.append("No."+str(l[x])+" crossed No."+str(hero)+". No."+str(hero)+" moved to postion " +str(x+1))
                x+=1
            l.pop(pos-1)
            l.insert(movep-1,hero)
        elif(pos == 10):
            movep = random.choice(range(1,10))
            while(x!=movep):
                comm.append("No."+str(hero)+" crossed No."+str(l[x-2])+". No."+str(hero)+" moved to postion "+str(x-1))
                x-=1
            l.pop(pos-1)
            l.insert(movep-1,hero)
        count+=1
    if(flagb == '3'):
        if(search(l,hero)==1):
            flagdis = "Congratulations, you won Rs."+ str(3*float(amount))+"!!"
            amount = float(amount)*3
        else:
            flagdis = "Sorry comrade!, Better luck next time"
            amount = 0
    elif(flagb=='2'):
        if(search(l,hero)==1 or search(l,hero)==2):
            flagdis = "Congratulations, you won Rs."+ str(2*float(amount))+"!!"
            amount = float(amount)*2
        else:
            flagdis = "Sorry comrade!, Better luck next time"
            amount = 0
    elif(flagb=='1.5'):
        if(search(l,hero)==1 or search(l,hero)==2 or search(l,hero)==3):
            flagdis = "Congratulations, you won Rs."+ str(1.5*float(amount))+"!!"
            amount = float(amount)*1.5
        else:
            flagdis = "Sorry comrade!, Better luck next time"
            amount = 0
    return render_template('com.html',comm = comm,flagdis = flagdis,flagb=flagb,amount = amount,usern=usern)