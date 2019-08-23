from flask import Flask, render_template, request
from selenium import webdriver
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

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
    #converts the multipled number into string because this fuction apparently can only retrun a string
    #return str(n)
    #return render_template('pass.html', n=name)
    iris = load_iris()

    x = iris.data
    y = iris.target
    #print(x.shape)
    #print(y.shape)
    #print(y.shape)

    #instantiating k meains algorithm
    knn = KNeighborsClassifier(n_neighbors=1)
    #print(knn)
    knn.fit(x,y)
    #n = input("Enter a number: ")
    a = float(knn.predict([[n1,n2,n3,n]]))
    if a==2:
        return "iris"
    elif a==1:
        return "iris again"
    else:
        return "no iris"

if __name__ == '__main__':
    app.Run(debug=True)