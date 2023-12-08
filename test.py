import uuid
from flask import Flask, jsonify, request, session
import mysql.connector as MC

app = Flask(__name__)

conn=MC.connect(host='localhost',database="testapi",user='root',password='')
cursor=conn.cursor()

req="SELECT * FROM boisson"
cursor.execute(req)

boissonlist=cursor.fetchall()

#pour lancer flask : flask\Scripts\activate
#executer le fichier py : python test.py
#installer le connecteur a la bdd:  pip install mysql-connector-python

#Commande supplémentaire
#virtualenv -p python3 flask
#python -m pip install flask


@app.route("/")
def accueil():
    return "Bienvenue"

@app.route("/liste")
def getAllBoisson():
    return jsonify(boissonlist)


@app.route("/hello/<name>")
def hello(name):
    return "Bonjour {}".format(name)

@app.route("/calcul/<int:a>/<int:b>")
def addition(a,b):
    return format(a*b)




# Lancement de l'application
if __name__ == '__main__':
    app.debug == True
    app.run()