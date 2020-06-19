from flask import Flask, redirect, url_for, request
app = Flask(__name__)
app.debug = True
from search import *
from store import *
from options import *
from ins import *
from add import *
from com import *
from deduct import *
from add_w import * 
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug = True) 
