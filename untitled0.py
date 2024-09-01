# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:45:32 2024

@author: hp
"""
import undetected_chromedriver as uc

from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome


import pandas as pd
import numpy as np
import re


import time

# Path to chromedriver.exe with raw string literal
path = r"C:\Users\21697\OneDrive\Bureau\chromedriver-win64\chromedriver.exe"

service = Service(path)


# Initialiser le WebDriver Chrome avec le service

# Récupérer le contenu HTML de la page

# Initialize the Chrome WebDriver with the service
driver = Chrome(service=service)






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

locations=[]
all_divs=[]

 
while True :


             
 last_height = driver.execute_script("return document.body.scrollHeight")
 time.sleep(4)
 page_source = driver.page_source
 soup = BeautifulSoup(page_source, 'html.parser')

# Find all the elements with the class "s-e-title-c"
 elements = soup.find_all('div', class_='s-e-title-c')
 




# Iterate over each element
 for article in elements:
    # Find the <h3> element within the current <div> element
    h3 = article.find('h3')
    
    if h3 and h3.text.rstrip("0123456789") not in names:
        names.append(h3.text.rstrip("0123456789"))

# Print the list of names
 
 
 
 
 # Trouver tous les éléments <p> avec la classe 'lead'
 #p_elements = soup.find_all('p', class_='lead')

# Parcourir tous les éléments <p> trouvés
# for p_element in p_elements:
    # Trouver l'élément <strong> à l'intérieur de chaque élément <p>
#    strong_element = p_element.find('strong')
 #   if strong_element:
#        text = strong_element.text.strip()
 #       if text not in dates:
 #        dates.append(text)
        
 
 
 try:
  secteur1= soup.findAll('div',class_="lpt-dropdown-counter")
  print(secteur1)
  secteur1=[sc.text.replace('\n','').strip("+ 123456789\n/") for sc in secteur1]
  print(secteur1)
  secteur1=[sc.replace('   ',',') for sc in secteur1]
 
        
           
  nombre=soup.select('span.count')
  nombre=[nb.text.strip("+ ")  for nb in nombre ]

  nombre=[int(nb) for nb in nombre]
  
  i=0
 
  for nb in nombre:
      if ",".join(secteur1[i:i+nb+1]) not in secteurs:
       secteurs.append(",".join(secteur1[i:i+nb+1]))
      i=i+nb+1
 except:
     secteurs.append("")
     
 
     


     



 
 
 description=soup.select('div.s-u-summary')
 try:

  for d in description :
    if  d.text not in descriptions:
      descriptions.append(d.text)
 except:
     descriptions.append("")

 els = soup.find_all('a', class_='startup-entry-hitbox')

# Iterate over each element
 for element in els:
    href_value = element.get('href')
    if href_value and "https://lespepitestech.com"+href_value not in sites_web:
        sites_web.append("https://lespepitestech.com"+href_value)

 driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
 
 time.sleep(5)   
 new_height = driver.execute_script("return document.body.scrollHeight")
 time.sleep(3)
 if new_height == last_height:
        print("Reached the bottom of the page.")
        break
import undetected_chromedriver as uc

from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome


import pandas as pd
import numpy as np
import re


import time

# Path to chromedriver.exe with raw string literal
path = r"C:\Users\21697\OneDrive\Bureau\chromedriver-win64\chromedriver.exe"

service = Service(path)


# Initialiser le WebDriver Chrome avec le service

# Récupérer le contenu HTML de la page

# Initialize the Chrome WebDriver with the service
driver = Chrome(service=service)






# URL du site web à ouvrir
url = "https://lespepitestech.com"
#adeplacer
# Initialiser le WebDriver Chrome


# Ouvrir l'URL spécifiée dans le navigateur
driver.get(url)
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')
coo=[]
linkdinks=[]
sites=[]
jaimes=[]
l=len(names)

for href in sites_web:
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

        # Naviguer vers l'URL
    driver.get(href)
        
        
    time.sleep(3)   
    # Extract data using BeautifulSoup
    fname_spans = soup.find_all('span', class_='fname')
    for s in fname_spans:
        if s.text not in coo:
            coo.append(s.text)

    btn_links = soup.find_all('a', class_='btn btn-default')
    for si in btn_links:
        href = si.get('href')
        if href and href not in sites:
            sites.append(href)

    linkedin_links = soup.find_all('a', class_='btn btn-just-icon btn-linkedin')
    for l in linkedin_links:
        href = l.get('href')
        if href and href not in linkdinks:
            linkdinks.append(href)
        elif not href:
            linkdinks.append("")

    try:
          likes_element = soup.find('div', class_='alternate-votes-display')
         
          value = likes_element.get_text()
      
          jaimes.append(int(value.rstrip()))
    except :
            jaimes.append(0)


    
    # Revenir à la page principale
driver.get(url)
driver.close()

# Afficher les résultats




# Save the DataFrame to an Excel file
m=min(len(names),len(coo),len(sites),len(linkdinks),len(jaimes),len(secteurs))
for n in names :
    n.rstrip("0123456789")
def enlever_chiffres(nom):
    return re.sub(r'\d+', '', nom)


names1=names[:m]
sites1=sites[:m]
linkdinks1=linkdinks[:m]
coo1=coo[:m]
descriptions1=descriptions[:m]
jaimes1=jaimes[1:m+1]
secteurs1=secteurs[:m]
def highlight_not_found(s):
    if s == "NOT FOUND":
        return 'color: red'
    else:
        return ''

coo1=[enlever_chiffres(nom) for nom in coo1]
data = {
    "Name": names1,
    "Website": sites1,
    "LinkedIn": linkdinks1,
    "Coordinator": coo1,
    "Secteur":secteurs1,
    "Description":descriptions1,
    "NB_JAIME":jaimes1,
   
}



df = pd.DataFrame(data)


# Replace empty strings with NaN
df.replace("", np.nan, inplace=True)



missing_values=df.isnull().sum()
# Use fillna to fill NaN values


styled_df = df.style.applymap(highlight_not_found)

output_path = r"C:\Users\21697\OneDrive\Bureau\lespepitestech_datafinal6.xlsx"

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





    
