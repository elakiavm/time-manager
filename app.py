'''
Created on 
    10th, Aug 2022
Course work: 
    Random TTC
@author: Elakia, Sugathan

Source:
    
'''
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():

    return ('hello world')

if __name__== "__main__":
    
    app.run(
        host    = "0.0.0.0", 
        debug   = True, 
        port    = 3848
    )