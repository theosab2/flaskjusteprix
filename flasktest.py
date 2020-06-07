from flask import Flask, render_template, request, json
import array
from datetime import datetime
import requests, json, random
import bs4

url = "https://api.cdiscount.com/OpenApi/json/Search"
params = {
          "ApiKey": "818e864c-7f59-41db-8546-6498f3d90ef0",
          "SearchRequest": {
            "Keyword": "masque",
            "Pagination": {
              "ItemsPerPage": 10,
              "PageNumber": 1
            },
            "Filters": {
              "Price": {
                "Min": 0,
                "Max": 0
              },
              "Navigation": "clavier",
              "IncludeMarketPlace": "false"
            }
          }
        }

response = requests.post(url, data=json.dumps(params))
price = []
picture = []
prNom = []
choix = []
resultat = []
reponse = ""
value = 0
k = 0
while k < 9:
    price.append(response.json()['Products'][k]['BestOffer']['SalePrice'])
    picture.append(response.json()['Products'][k]['MainImageUrl'])
    prNom.append(response.json()['Products'][k]['Name']) 
    k += 1

app = Flask(__name__)
k = 0
listPrix = []

@app.route('/', methods=['get','post'])
def index():
    global value
    if(request.method == 'POST'):
        nombre = request.form.get('nombre')
        if(nombre == ""):
            return render_template('index.html')
        else:
            if(nombre < price[value]):
                reponse = "plus grand"
            elif(price[value] < nombre):
                reponse = "plus petit"
            else:
                reponse = "gagné"

            choix.append({
                'nombre': nombre,
                'reponse': reponse, 
            })

            resultat = {
                'reponse': reponse,
                'nombre' : nombre,
                'choix' : choix
            }
            return render_template('index.html', choix = choix, resultat = resultat, prix = price[value],imgPr =picture[value], prNom = prNom[value])
    else:
        i = 0
        while i < len(choix):
            choix.pop(i)

        value = int(9*random.random())
        return render_template('index.html',prix = price[value], listPrix=listPrix, imgPr =picture[value], prNom = prNom[value])

if __name__ == '__main__':
    app.run(debug=True, host='localhost')    


