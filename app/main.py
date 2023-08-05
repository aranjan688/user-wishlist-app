from flask import Flask , render_template, request
import redis
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://hello_flask:hello_flask@db:5432/hello_flask_dev'
red =redis.Redis(host='redis',port=6379)

from models import db , UserFavs

@app.route("/")
def main():
    return render_template("index.html")
    
@app.route("/save" ,methods=["POST"])
def save():
    username = request.form['username']
    place = request.form['place']
    food = request.form['food']
    print("username:" , username)
    
    
    if red.hgetall(username).keys():
        print("hget username" ,red.hgetall(username))
    else:
        print("no such username")
    
    return "entered save"





        