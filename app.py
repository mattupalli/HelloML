from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getVal():
    name= request.form['name']
    #converts string into int and multiplies by 2
    n= (int(name))*2
    #converts the multipled number into string because this fuction apparently can only retrun a string
    return str(n)
    #return render_template('pass.html', n=name)

if __name__ == '__main__':
    app.Run(debug=True)
