from flask import Flask, render_template
from m import app
import random
@app.route('/home/<usern>')
def home(usern):
    file = open("races.txt", "r")
    li_races = file.readlines()
    file.close()
    li_of_races = []
    race = []
    i = 0
    for lines in li_races:
        if i%3 == 0 and i != 0:
            li_of_races.append(race)
            race = []
        race.append(lines)
        i += 1
    ran_li = []
    j = 0
    while(j < 5):
        if random.choice(li_of_races) in ran_li:
            j -= 1
        else:
            ran_li.append(random.choice(li_of_races)) 
        j += 1
    
    return render_template('home.html', ran_li = ran_li, usern = usern, title = 'Home')

@app.route('/profile/<usern>')
def profile(usern):
    file = open("1.txt", "r")
    credentials = file.readlines()
    i = 0
    while(credentials[i] != 'end\n'):
        if(credentials[i] == usern + str('\n')):
            us_n = credentials[i]
            i += 2
            us_a = credentials[i]
            i += 1
            us_g = credentials[i]
            i+=1
            us_dob = credentials[i]
            i+=1
            us_m = credentials[i]
            break
        i += 1
    return render_template('profile.html', us_n = us_n, us_a = us_a, us_m = us_m,us_g=us_g,us_dob=us_dob, usern = usern, title = 'profile')

@app.route('/horses/<usern>')
def horses(usern):
    file = open("horses.txt", "r")
    li_horses = file.readlines()
    file.close()
    li_of_horses = []
    horse = []
    i = 0
    for lines in li_horses:
        if i%5 == 0 and i != 0:
            li_of_horses.append(horse)
            horse = []
        horse.append(lines)
        i += 1
    ran_li = []
    j = 0
    while(j < 10):
        if random.choice(li_of_horses) in ran_li:
            j -= 1
        else:
            ran_li.append(random.choice(li_of_horses))
        j += 1
    return render_template('horses.html', ran_li = ran_li, usern = usern)

@app.route('/type/<value>/<usern>')
def type(usern,value):
    return render_template('type.html', usern = usern,value = value)


'''if __name__ == '__main__' :
    app.run(debug = True)'''
