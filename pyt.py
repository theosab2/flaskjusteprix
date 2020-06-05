#!/usr/bin/env python
# -*- coding: utf­-8 ­-*-


#annee = int(input())
#if annee % 4 == 0:
#    if annee % 100 == 0:
#        if annee % 400 ==0:
#
#            print("oui")
#       else:
#            print("non")    
#    else:
#       print("non")        
#else:
#    print("non")
    
#recette = {"farine" : {"quantite": 20 , "unite": "g" },
#       "oeuf" : {"quantite": 0.2, "unite": ""},
#       "lait" : { "quantite": 0.05 , "unite": "L"},
#       "huile": { "quantite": 0.001 , "unite": "L"},
#       "rhum": { "quantite": 0.001, "unite": "L" }}
 
#print("Pour faire une crepe, il faut")
#for ingredient, quantite in recette.items():
#    print("- {} {} de {}".format(quantite['quantite'], quantite['unite'], ingredient))

#def recette_pour(nb_crepe=5):
#    print("Pour faire "+str(nb_crepe)+" crêpes, il faut :")
#    for ingredient, quantite in recette.items():
#        print("- {} {} de {}".format(quantite['quantite']*nb_crepe, quantite['unite'], ingredient))

#def recette_personne(nb_personne=1):
#    print("\nRecette des crêpes pour "+str(nb_personne)+" (5 crêpes/personne) \n")
#    recette_pour(nb_personne*5)

# recette_pour(5)
# recette_personne(4)
#crepe_par_personne = int(input("Combien de crepe mange une personne ? "))
#nombre_de_personne = int(input("Combien de personne vous manger des crepes ? "))
#recette_pour(crepe_par_personne)
#recette_personne(nombre_de_personne)



#import requests
#from bs4 import BeautifulSoup
#import os
 
#result = requests.get('https://www.commitstrip.com/fr/')
# print(result.text)
#soup = BeautifulSoup(result.text, features="html.parser")
 
#pages = soup.find('span', attrs={"class": u"pages"})
#length = pages.text.split()[-1]
 
#for i in range(1, int(length) + 1):
#    print(i)
#    page_result = requests.get('https://www.commitstrip.com/page/'+str(i))
#    page_soup = BeautifulSoup(page_result.text, features="html.parser")
#   articles = page_soup.find('div', attrs={"class": u"excerpts"})
#    links = articles.find_all('a')
#    for link in links:
#        result = requests.get(link['href'])
#        articleSoup = BeautifulSoup(result.text, features="html.parser")
#        img = articleSoup.find('img', attrs={"class": u"size-full"})
# 
#        filename = img['src'].split('/')[-1]
#        if 'Strip' in filename:
#            print(filename)
#            r = requests.get(img['src'], allow_redirects=True)
#            open(filename, 'wb').write(r.content)

#!/usr/bin/env python
# coding=utf-8

import csv, json, sys
from itertools import islice

"""
- Top 3 des prénoms masculins attribués de 1900 à 2017 en Seine Maritime
- Top 1 des prénoms féminins attribués par département en 2016
- Top 10 des prénoms féminins attribués dans le pays entier en 2016
"""

#### CODE COMMUN AUX 3 PARTIES
# Je défini mon fichier source
fname = "dpt2017.txt"
# Exemple de code compatible python 2 ET 3
if sys.version_info[0] == 2:
    file = open(fname, "r")
else:
    file = open(fname, "r", encoding='utf8')

### En observant le fichier on s'aperçoit que c'est un CSV délimité par des tabulations "\t"
### Row 0 = sexe (1 homme 2 femme)
### Row 1 = Prenom
### Row 2 = annee
### Row 3 = département
### Row 4 = nombre

### 1ERE PARTIE : Top 3 des prénoms masculins attribués de 1900 à 2017 en Seine Maritime
print("\n### PARTIE 1 : Top 3 des prénoms masculins attribués de 1900 à 2017 en Seine Maritime ###\n")
reader = csv.reader(file, delimiter="\t")
list_prenom_filtres = list()
### Extraction du CSV des "hommes" (row[0]=1) qui sont du département seine maritime (row[3]=76)
for row in reader:
    if str(1) in row[0] and str(76) in row[3]:
        # print("homme 76 = "+str(row))
        if row[1] != "_PRENOMS_RARES":
            list_prenom_filtres.append([row[1],row[2],row[4]])
# print("list_prenom_filtres="+str(list_prenom_filtres))
### Seconde boucle dans les prenoms prefiltre afin de faire les totaux
i = 0
total = 0
result = []
### Pour chaque prenom de la liste prefiltre
for prenom in list_prenom_filtres:
    ### si le prenom est egal au précédent
    if prenom[0] == list_prenom_filtres[i-1][0]:
        ### on ajoute le total de cette ligne pour ce prenom
        total += int(prenom[2])
        ### quand on tombe sur un prenom qui n'est pas egale au suivant on update notre liste avec le total de ce prenom
        if prenom[0] != list_prenom_filtres[i+1][0]:
            result.append({'prenom': prenom[0], 'total': total})
        # print("prenom="+str(prenom[0])+" / total="+str(total))
    ### Sinon le total est egale a la ligne de ce prenom (si le prenom n'est pas = au précédent)
    else:
        total = int(prenom[2])
        # print("prenom suivant ="+str(list_prenom_filtres[i-1][0])+"total reset")
    i += 1
### On liste les résultats en triant par les valeurs de la clé "total" afin de n'en sortir que les 3 premiers
pretty_output = list(islice(sorted(result, key=lambda x: x['total'], reverse=True),3))
# print(json.dumps(pretty_ouput, indent=4, ensure_ascii=False))
print("On a parcouru "+str(i)+" prénoms, le top 3 est :")
for item in pretty_output:
    print("  -"+str(item["prenom"]+ " == > "+str(item["total"])+" naissances entre 1900 et 2017"))

### 2EME PARTIE : Top 1 des prénoms féminins attribués par département en 2016
print("\n### PARTIE 2 : Top 1 des prénoms féminins attribués par département en 2016 ###\n")
reader = csv.reader(open(fname), delimiter="\t")
list_prenom_filtres = list()
### Extraction du CSV des "femmes" (row[0]=2) de 2016
for row in reader:
    if str(2) in row[0] and str(2016) in row[2]:
        # print("femme 2016 = "+str(row))
        if row[1] != "_PRENOMS_RARES":
            list_prenom_filtres.append([row[1],row[3],row[4]])
# print("list_prenom_filtres="+str(list_prenom_filtres))

i = 0
total = 0
result_list = []
result = {}
# Construction d'une liste des départements a parcourir
# departements = list(range(1,96))+list(range(971,977))+["2A","2B"]
REGIONS = {
    'Auvergne-Rhône-Alpes': ['01', '03', '07', '15', '26', '38', '42', '43', '63', '69', '73', '74'],
    'Bourgogne-Franche-Comté': ['21', '25', '39', '58', '70', '71', '89', '90'],
    'Bretagne': ['35', '22', '56', '29'],
    'Centre-Val de Loire': ['18', '28', '36', '37', '41', '45'],
    'Corse': ['2A', '2B'],
    'Grand Est': ['08', '10', '51', '52', '54', '55', '57', '67', '68', '88'],
    'Guadeloupe': ['971'],
    'Guyane': ['973'],
    'Hauts-de-France': ['02', '59', '60', '62', '80'],
    'Île-de-France': ['75', '77', '78', '91', '92', '93', '94', '95'],
    'La Réunion': ['974'],
    'Martinique': ['972'],
    'Normandie': ['14', '27', '50', '61', '76'],
    'Nouvelle-Aquitaine': ['16', '17', '19', '23', '24', '33', '40', '47', '64', '79', '86', '87'],
    'Occitanie': ['09', '11', '12', '30', '31', '32', '34', '46', '48', '65', '66', '81', '82'],
    'Pays de la Loire': ['44', '49', '53', '72', '85'],
    'Provence-Alpes-Côte d\'Azur': ['04', '05', '06', '13', '83', '84'],
}
departements = {
    '01': 'Ain',
    '02': 'Aisne',
    '03': 'Allier',
    '04': 'Alpes-de-Haute-Provence',
    '05': 'Hautes-Alpes',
    '06': 'Alpes-Maritimes',
    '07': 'Ardèche',
    '08': 'Ardennes',
    '09': 'Ariège',
    '10': 'Aube',
    '11': 'Aude',
    '12': 'Aveyron',
    '13': 'Bouches-du-Rhône',
    '14': 'Calvados',
    '15': 'Cantal',
    '16': 'Charente',
    '17': 'Charente-Maritime',
    '18': 'Cher',
    '19': 'Corrèze',
    '2A': 'Corse-du-Sud',
    '2B': 'Haute-Corse',
    '21': 'Côte-d\'Or',
    '22': 'Côtes-d\'Armor',
    '23': 'Creuse',
    '24': 'Dordogne',
    '25': 'Doubs',
    '26': 'Drôme',
    '27': 'Eure',
    '28': 'Eure-et-Loir',
    '29': 'Finistère',
    '30': 'Gard',
    '31': 'Haute-Garonne',
    '32': 'Gers',
    '33': 'Gironde',
    '34': 'Hérault',
    '35': 'Ille-et-Vilaine',
    '36': 'Indre',
    '37': 'Indre-et-Loire',
    '38': 'Isère',
    '39': 'Jura',
    '40': 'Landes',
    '41': 'Loir-et-Cher',
    '42': 'Loire',
    '43': 'Haute-Loire',
    '44': 'Loire-Atlantique',
    '45': 'Loiret',
    '46': 'Lot',
    '47': 'Lot-et-Garonne',
    '48': 'Lozère',
    '49': 'Maine-et-Loire',
    '50': 'Manche',
    '51': 'Marne',
    '52': 'Haute-Marne',
    '53': 'Mayenne',
    '54': 'Meurthe-et-Moselle',
    '55': 'Meuse',
    '56': 'Morbihan',
    '57': 'Moselle',
    '58': 'Nièvre',
    '59': 'Nord',
    '60': 'Oise',
    '61': 'Orne',
    '62': 'Pas-de-Calais',
    '63': 'Puy-de-Dôme',
    '64': 'Pyrénées-Atlantiques',
    '65': 'Hautes-Pyrénées',
    '66': 'Pyrénées-Orientales',
    '67': 'Bas-Rhin',
    '68': 'Haut-Rhin',
    '69': 'Rhône',
    '70': 'Haute-Saône',
    '71': 'Saône-et-Loire',
    '72': 'Sarthe',
    '73': 'Savoie',
    '74': 'Haute-Savoie',
    '75': 'Paris',
    '76': 'Seine-Maritime',
    '77': 'Seine-et-Marne',
    '78': 'Yvelines',
    '79': 'Deux-Sèvres',
    '80': 'Somme',
    '81': 'Tarn',
    '82': 'Tarn-et-Garonne',
    '83': 'Var',
    '84': 'Vaucluse',
    '85': 'Vendée',
    '86': 'Vienne',
    '87': 'Haute-Vienne',
    '88': 'Vosges',
    '89': 'Yonne',
    '90': 'Territoire de Belfort',
    '91': 'Essonne',
    '92': 'Hauts-de-Seine',
    '93': 'Seine-Saint-Denis',
    '94': 'Val-de-Marne',
    '95': 'Val-d\'Oise',
    '971': 'Guadeloupe',
    '972': 'Martinique',
    '973': 'Guyane',
    '974': 'La Réunion',
    '976': 'Mayotte',
}
for departement in sorted(departements.keys()):
    # conversion des départements de type int en string et ajout du 0 devant les départements < 10 (pour matcher avec le modèle du fichier CSV)
    # try:
    #     if int(departement) < 10:
    #         departement = str("0")+str(departement)
    #     else:
    #         departement = str(departement)
    # except ValueError:
    #     #print("les départements "+departement+" sont déjà des strings")
    #     pass
    for item in list_prenom_filtres:
        if departement == item[1]:
            result_list.append({"prenom":item[0], "nombre": item[2]})
            result.update({item[1]:result_list})
    #print("Departement = "+str(departement))
    dpt_output = list(islice(sorted(result_list, key=lambda x: int(x['nombre']), reverse=True),1))
    #print(json.dumps(dpt_output, indent=4, ensure_ascii=False))
    try:
        print("Il y a eu "+str(dpt_output[0]["nombre"])+" "+str(dpt_output[0]["prenom"])+" en 2016 dans le département "+str(departements[departement])+" ("+departement+")")
    except IndexError:
        print("Il n'y a pas assez de données en 2016 dans le département "+str(departements[departement])+" ("+departement+")")
    result_list=[]

### 3EME PARTIE : Top 10 des prénoms féminins attribués dans le pays entier en 2016
print("\n### PARTIE 3 : Top 10 des prénoms féminins attribués dans le pays entier en 2016 ###\n")
reader = csv.reader(open(fname), delimiter="\t")
list_prenom_filtres = list()

### Extraction du CSV des "femmes" (row[0]=2) qui sont de 2016 (row[2]=2016)
for row in reader:
    if str(2) in row[0] and str(2016) in row[2]:
        # filtre prenom rares qui n'est pas un prenom...
        if row[1] != "_PRENOMS_RARES":
            list_prenom_filtres.append([row[1],row[4]])
# print("list_prenom_filtres="+str(len(list_prenom_filtres)))

i = 0
total = 0
result = []
### Pour chaque prenom de la liste prefiltre
for prenom in list_prenom_filtres:
    ### si le prenom est egal au précédent
    if prenom[0] == list_prenom_filtres[i-1][0]:
        ### on ajoute le total de cette ligne pour ce prenom
        total += int(prenom[1])
        # print(prenom[0],total)
        ### quand on tombe sur un prenom qui n'est pas egale au suivant on update notre liste avec le total de ce prenom
        try:
            if prenom[0] != list_prenom_filtres[i+1][0]:
                result.append({'prenom': prenom[0], 'total': total})
                # print(str(type(prenom[0]))+"/"+prenom[0])
        except IndexError:
            break
    ### Sinon le total est egale a la ligne de ce prenom (si le prenom n'est pas = au précédent)
    else:
        total = int(prenom[1])
    i += 1

### On liste les résultats en triant par les valeurs de la clé "total" afin de n'en sortir que les 3 premiers
pretty_output = list(islice(sorted(result, key=lambda x: x['total'], reverse=True),10))
# print(json.dumps(pretty_output, indent=4, ensure_ascii=False))
print("On a parcouru "+str(i)+" prénoms, le top 10 de 2016 est :")
for item in pretty_output:
    print("  -"+str(item["prenom"]+ " == > "+str(item["total"])+" naissances en 2016"))

## Exemple de sortie vers un fichier
# with open('data.txt', 'w') as outfile:
#     json.dump(pretty_output, outfile)
