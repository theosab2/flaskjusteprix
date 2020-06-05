from flask import Flask, render_template, request
import array

app = Flask(__name__)
k = 0
listPrix = []
@app.route('/', methods=['get','post'])
def index():
    global k
    k += 1
    occurence = k
    prix = 12

    return render_template('index.html', title = prix, listPrix=listPrix)

@app.route('/', methods=['get','post'])
def addEle():
    global k
    global listPrix
    n = request.form['nombre']
    listPrix.append(n)
    print(n)
    prix = 12
    print("test = ",n )
    return render_template('index.html', title = prix, listPrix=listPrix, test = request.form['nombre'])

if __name__ == '__main__':
    app.run(debug=True, host='localhost')    


