#!/usr/bin/env python
# -*- coding: utf­-8 ­-*-
#from flask import Flask
import requests, json
#app = Flask(__name__)
#@app.route('/')
url = "https://api.cdiscount.com/OpenApi/json/Search"
params = {
          "ApiKey": "818e864c-7f59-41db-8546-6498f3d90ef0",
          "SearchRequest": {
            "Keyword": "clavier",
            "Pagination": {
              "ItemsPerPage": 1,
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
#['Products'][0]['BestOffer']['SalePrice']
print(response.json())
#
"""
prixArticle = x
reponse = "?"
while True:
    nbEntre = int(input("Entrez un nombre"))
    if nbEntre < prixArticle :
        reponse = "Moin cher"
        print(nbEntre, reponse)
    else :
        reponse = "Plus cher"
        print(nbEntre, reponse)
    if nbEntre == prixArticle:
        reponse = "Gagné"
        print(nbEntre, reponse)
        break


import requests, json
 
{
  "ApiKey": "818e864c-7f59-41db-8546-6498f3d90ef0",
}
 
params = {
          "ApiKey": "818e864c-7f59-41db-8546-6498f3d90ef0",
          "SearchRequest": {
            "Keyword": "clavier",
            "Pagination": {
              "ItemsPerPage": 1,
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
    
   
 
url = "https://api.cdiscount.com/OpenApi/json/Search"
    
r = requests.post(url, data=json.dumps(params))
 
print(r.json())
"""