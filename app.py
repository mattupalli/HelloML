from flask import Flask, render_template, request
from selenium import webdriver
import sklearn
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getVal():
    name= request.form['name']
    name1=request.form['name1']
    name2=request.form['name2']
    name3=request.form['name3']
    #converts string into int and multiplies by 2
    n= (int(name))
    n1=(int(name1))
    n2=(int(name2))
    n3=(int(name3))
    model = pickle.load(open('saved_model.pkl','rb'))
    a = int(model.predict([[n,n1,n2,n3]]))
    return render_template('index.html',num=a)

if __name__ == '__main__':
    app.Run(debug=True)