from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    #return render_template('index.html')
    return '<h1>Deployed</h1>'

#@app.route('/', methods=['POST'])
#def getVal():
 #   return '<h1>Deployed</h1>'
    #name= request.form['name']
    #converts string into int and multiplies by 2
    #n= (int(name))*2
    #converts the multiples number into string back beacause this fuction apparently can only retrun a string
    #return str(n)
    #return render_template('pass.html', n=name)

#if __name__ == '__main__':
#   app.Run(debug=True)