from bs4 import BeautifulSoup
import urllib.request

import pandas as pd

def recrute_scraping(number):
  #url = input("Entrez l'url :")
  number=str(number)
  #new_url = f"https://www.rekrute.com/offres.html?st=d&keywordNew=1&keyword={word}&filterLogo=&filterLogo=&filterLogo=&filterLogo="
  new_url=f"https://www.rekrute.com/offres.html?p={number}&s=1&o=1&query=data+scientist&keyword=data+scientist&st=d"
  print(new_url)
  webpage = urllib.request.urlopen(new_url)

  soup = BeautifulSoup(webpage,"html.parser")
  results=soup.find_all("div", {"class": "col-sm-10 col-xs-12"})
  titles = []
  descs = []
  entres=[]
  objecs=[]
  publis=[]
  secteurs=[]
  for result in results:
    title = result.find("a").text
    titles.append(title)


    try :
      description_du_poste = result.find("span", { "style": "color: #5b5b5b; font-style : italic;"}).text
    except :
      description_du_poste = result.find("span", { "style": "color: #5b5b5b;margin-top: 5px;"}).text
 

    descs.append(description_du_poste)
    # print(f" Description du poste : {description_du_poste.text} ")  
    # print(description_du_poste)

    entreprise = result.find("span", { "style": "color: #5b5b5b;"}).text
    entres.append(entreprise)
  # print(f" Entreprise: {entreprise.text} ")
    # print(entreprise) 

    objectif  = result.find("span", { "style": "color: #5b5b5b;margin-top: 5px;"}).text
    objecs.append(objectif)
  # print(f" Objectif de la mission : {objectif.text} ") 

    publication= result.find("em", { "class": "date"}).text
    publis.append(publication)
  # print(f" Publication et nombres de poste  : {publication.text} ") 

    secteur= result.find("li").text.replace(' \n' , '')
    secteurs.append(secteur)
    # print(secteur)
  # print(f" Secteur d'activité : {secteur.text} ")
  
  data = pd.DataFrame.from_dict({'title':titles, 'description_du_poste':descs,'entreprise':entres,'objectif':objecs,'publication':publis,'secteur':secteurs})

  return data
  #file_name = input('le nom du fichier excel : ')
 # data.to_excel(file_name+'.xlsx', index=False)
liste_of_datas =  []
for i in range(1,5):

  data=recrute_scraping(i)
  liste_of_datas.append(data)

data_frame=pd.concat(liste_of_datas,axis=0).reset_index(drop=True)
file_name = input('le nom du fichier excel : ')
data_frame.to_excel(file_name+'.xlsx', index=False)

