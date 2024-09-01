# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 18:18:14 2024

@author: hp
"""

"""
Created on Fri Jun 28 16:45:32 2024

@author: hp
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np
import re


import time
# Récupérer le contenu HTML de la page


# Path to chromedriver.exe with raw string literal
path = r"C:\Users\21697\OneDrive\Bureau\chromedriver-win64\chromedriver.exe"

service = Service(path)


# Initialiser le WebDriver Chrome avec le service
driver = webdriver.Chrome(service=service)

# URL du site web à ouvrir
url = "https://lespepitestech.com"
#adeplacer
# Initialiser le WebDriver Chrome


# Ouvrir l'URL spécifiée dans le navigateur
driver.get(url)
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')


secteurs=[]    
sites_web=[]

names=[] 
descriptions=[]
dates=[]
jaimes=[]
locations=[]

 
while True :


             
 last_height = driver.execute_script("return document.body.scrollHeight")
 time.sleep(2)
 page_source = driver.page_source
 soup = BeautifulSoup(page_source, 'html.parser')

# Find all the elements with the class "s-e-title-c"
 elements = soup.find_all('div', class_='s-e-title-c')
 




# Iterate over each element
 for article in elements:
    # Find the <h3> element within the current <div> element
    h3 = article.find('h3')
    
    if h3 and h3.text not in names:
        names.append(h3.text.rstrip("0123456789"))

# Print the list of names
 print(names)
 article_nb = soup.find_all('h3')
 print(h3)
 
 
 # Trouver tous les éléments <p> avec la classe 'lead'
 p_elements = soup.find_all('p', class_='lead')

# Parcourir tous les éléments <p> trouvés
 for p_element in p_elements:
    # Trouver l'élément <strong> à l'intérieur de chaque élément <p>
    strong_element = p_element.find('strong')
    if strong_element:
        text = strong_element.text.strip()
        dates.append(text)
        
 
 print(dates)
 try:
  secteur1= soup.select('div.lpt-dropdown-counter a')
  secteur1=[sc.text for sc in secteur1]
 
  nombre=soup.select('span.count')
  nombre=[nb.text.strip("+ ")  for nb in nombre ]
  nombre=[int(nb) for nb in nombre]
  i=0
 
  for nb in nombre:
     secteurs.append(",".join(secteur1[i:i+nb+1]))
     i=i+nb+1
 except:
     secteurs.append("")
     
 
 jaime=soup.select('div.alternate-votes-display')
 for jaim in jaime:
     jaimes.append(int(jaim.text))
 
     


     


 
 print(secteurs)
 print(jaimes)

 
 
 description=soup.select('div.s-u-summary')
 try:

  for d in description:
   descriptions.append(d.text)
 except:
     descriptions.append("")
 print(descriptions)
     
 els = soup.find_all('a', class_='startup-entry-hitbox')

# Iterate over each element
 for element in els:
    href_value = element.get('href')
    if href_value and href_value not in sites_web:
        sites_web.append(href_value)

 driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
 time.sleep(5)   
 new_height = driver.execute_script("return document.body.scrollHeight")
 if new_height == last_height:
        print("Reached the bottom of the page.")
        break

 
coo=[]
linkdinks=[]
sites=[]
for href in sites_web:

        # Naviguer vers l'URL
        driver.get(href)
        
        
        s=driver.find_element(By.XPATH, '//span[@class="fname"]')
        
        # Extraire le texte de l'élément <span> et l'ajouter à la liste
        if s.text not in coo:
         coo.append(s.text)
        si=driver.find_element(By.XPATH,'//a[@class="btn btn-default"]')
        if si.get_attribute('href') not in sites:
         sites.append(si.get_attribute('href'))
        try :
           l=driver.find_element(By.XPATH,'//a[@class="btn btn-just-icon btn-linkedin"]')
           if l.get_attribute('href') not in linkdinks:
            linkdinks.append(l.get_attribute('href'))
        except:
            linkdinks.append("")
    
    # Revenir à la page principale
driver.get(url)

# Afficher les résultats
print(coo)
print(linkdinks)

print(sites)

        
import re


# Save the DataFrame to an Excel file
m=min(len(names),len(coo),len(sites),len(linkdinks),len(dates),len(jaimes),len(secteurs))
for n in names :
    n.rstrip("0123456789")
def enlever_chiffres(nom):
    return re.sub(r'\d+', '', nom)


names=names[:m]
sites=sites[:m]
linkdinks=linkdinks[:m]
coo=coo[:m]
dates=dates[:m]
jaimes=jaimes[:m]
secteurs=secteurs[:m]
def highlight_not_found(s):
    if s == "NOT FOUND":
        return 'color: red'
    else:
        return ''

coo=[enlever_chiffres(nom) for nom in coo]
data = {
    "Name": names,
    "Website": sites,
    "LinkedIn": linkdinks,
    "Coordinator": coo,
    "Secteur":secteurs,
    "Date":dates,
    "NB_JAIME":jaimes
}



df = pd.DataFrame(data)


# Replace empty strings with NaN
df.replace("", np.nan, inplace=True)



missing_values=df.isnull().sum()
# Use fillna to fill NaN values
df.fillna("NOT FOUND", inplace=True)

styled_df = df.style.applymap(highlight_not_found)

output_path = r"C:\Users\21697\OneDrive\Bureau\lespepitestech_datafinal3.xlsx"

styled_df.to_excel(output_path, engine='openpyxl', index=False)

# Path to chromedriver.exe with raw string literal
#path = r"C:\Users\21697\OneDrive\Bureau\chromedriver-win64\chromedriver.exe"

#service = Service(path)

# Initialiser le WebDriver Chrome avec le service
#driver = webdriver.Chrome(service=service)

# URL du site web à ouvrir
#url = "https://lespepitestech.com"
#adeplacer
# Initialiser le WebDriver Chrome


# Ouvrir l'URL spécifiée dans le navigateur
#driver.get(url)
#driver.get("https://www.linkedin.com/login")
#time.sleep(3)
 
 
 
 
#with open ("user_name.txt") as f:
#  user_name=f.readline().strip()
#  password=f.readline().strip()

#driver.find_element(By.XPATH,'//input[@id="username"]').click()
#driver.find_element(By.XPATH,'//input[@id="username"]').send_keys(user_name)
#driver.find_element(By.XPATH,'//input[@id="password"]').click() 

#driver.find_element(By.XPATH,'//input[@id="password"]').send_keys(password)
#driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button').click()"""





    
