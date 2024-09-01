# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 08:10:25 2024

@author: hp
"""

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the Excel file
file_path =r"C:\Users\21697\OneDrive\Bureau\AI\stage formation humaine\lespepitestech_datafinal6.xlsx"
df = pd.read_excel(file_path)

# Step 2: Make a copy of the DataFrame and drop unnecessary columns
df1 = df.copy()
df1 = df1.drop(['Website', 'Name', 'Coordinator', 'LinkedIn', 'Description'], axis=1)
df_n=df1
# Step 3: Split 'Secteur' into lists of individual sectors
df1["Secteur"] = df1["Secteur"].apply(lambda x: x.split(','))

# Step 4: Explode the 'Secteur' column into multiple rows
df1 = df1.explode('Secteur')
df1=df1.groupby(['Secteur'])['NB_JAIME'].mean().reset_index()
# Step 5: Handle missing values (optional, based on the output of df1.isnull().sum())
df1 = df1.dropna()

# Step 6: Visualize the data
# Histogram of numerical columns


df1.hist(rwidth=0.9, figsize=(10, 8))
plt.xlabel("Number of likes")
plt.ylabel("Frequency")
plt.title("Histogramme of likes")
plt.tight_layout()
plt.show()
plt.savefig(r'C:/Users/21697/OneDrive/figure.png')




# Afficher le graphique
plt.show()
cat_list = df1['Secteur'].unique()
cat_average=df1.groupby('Secteur').mean()['NB_JAIME']
couleurs=['g','r','m','b']
plt.figure(figsize=(50, 8))  # Ajuste la taille de la figure à 10 pouces de largeur et 6 pouces de hauteur

plt.bar(cat_list[:100],cat_average[:100],color=couleurs)
# Amélioration de la visibilité des labels de l'axe des abscisses
plt.xticks(rotation=90)  # Pivote les labels de 45 degrés

# Ajouter les titres et labels
plt.xlabel('Secteur')
plt.ylabel('NB_JAIME')
plt.title('Nombre moyen de "J\'aime" par secteur')
plt.tight_layout()


# Afficher le graphique
plt.show()
plt.savefig(r'C:/Users/21697/OneDrive/figure2.png')
#Simple Regression lineaire 
from sklearn.metrics import mean_squared_error as MSE

x=df1.iloc[:,:-1].values
y=df1.iloc[:,-1].values
y=y.reshape(-1,1)
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
Regressor=LinearRegression()
import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
# Initialize LabelEncoder
encoder = LabelEncoder()

# Fit and transform the data
# Fit et transformation des données
x_flattened = np.array([str(item) for sublist in x for item in sublist])

x_encoded = encoder.fit_transform(x_flattened)
# Redimensionnement pour qu'il soit en 2D
x_encoded = x_encoded.reshape(-1, 1)
x_classe=encoder.classes_
# Affichage des valeurs encodées


# Affichage de la correspondance entre les catégories et les valeurs numériques
reg=pd.DataFrame({'SECTEUR':encoder.classes_,'Correspondance':x_encoded.flatten()})
output_path = r"C:\Users\21697\OneDrive\Bureau\lespepitestech_correspondance3.xlsx"
reg.to_excel(output_path, engine='openpyxl', index=False)
# Apply StandardScaler
scaler_x = StandardScaler()
scaler_y = StandardScaler()
x_scaled = scaler_x.fit_transform(x_encoded)
y_scaled = scaler_y.fit_transform(y)

# Split the data
X_train, X_test, Y_train, Y_test = train_test_split(x_scaled,y_scaled, test_size=0.2, random_state=3)





Regressor.fit(X_train,Y_train)
Y_predict=Regressor.predict(X_test)



plt.show()
mse1=MSE(Y_test,Y_predict)
x_grid = np.arange(min(X_train), max(X_train), 0.1).reshape(-1, 1)
plt.scatter(X_train, Y_train, color='blue')
plt.plot(x_grid, Regressor.predict(x_grid), color='red')
plt.title("Linear Regression: Predicted vs Actual")
plt.xlabel('SECTEUR (encoded)')
plt.ylabel('Likes')
plt.ylim(-0.5,0.2)
plt.show()
plt.savefig(r'C:/Users/21697/OneDrive/Regression1.png')

from sklearn.metrics import r2_score

# Prédiction et inverse de la transformation
r1 = r2_score(Y_test, Y_predict)
print(Regressor.predict([[-0.325]]))

#svr modele
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error as MSE


# Split the data

# Train the SVR model



svr_regressor = SVR(kernel='rbf',gamma=1.0)
svr_regressor.fit(X_train, Y_train)

# Predict the test set results
Y_predict = svr_regressor.predict(X_test)
plt.figure()
# Visualize the results
x_grid = np.arange(min(X_train), max(X_train), 0.1).reshape(-1, 1)
plt.scatter(X_train, Y_train, color='blue')
plt.plot(x_grid, svr_regressor.predict(x_grid), color='red')
plt.title("Prédire les secteurs les plus préférables")
plt.xlabel('Les différents secteurs (encodés et normalisés)')
plt.ylabel('Les nombres de j\'aimes (normalisés)')
plt.show()
mse2=MSE(Y_test,Y_predict)
from sklearn.metrics import r2_score

# Prédiction et inverse de la transformation
r2 = r2_score(Y_test, Y_predict)

##arbre 

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE

X_train1, X_test1, Y_train1, Y_test1 = train_test_split(x_encoded, y, test_size=0.3, random_state=3)



regressor1 = DecisionTreeRegressor(random_state=0, min_samples_split=10, max_depth=10,criterion="absolute_error")
regressor1.fit(X_train, Y_train)
Y_predict = regressor1.predict(X_test)
mse3 = MSE(Y_test, Y_predict)
plt.figure()
x_grid = np.arange(min(X_train), max(X_train), 0.1).reshape(-1, 1)
plt.scatter(X_train, Y_train, color='blue')
plt.plot(x_grid, regressor1.predict(x_grid), color='red')
plt.title("Prédire les secteurs les plus préférables")
plt.xlabel('Les différents secteurs (encodés et normalisés)')
plt.ylabel('Les nombres de j\'aimes (normalisés)')
plt.show()
from sklearn.metrics import r2_score

# Prédiction et inverse de la transformation
r3 = r2_score(Y_test, Y_predict)

#neighbor
from sklearn.metrics import mean_squared_error as MSE

from sklearn.ensemble import RandomForestRegressor

regressor2 = RandomForestRegressor(n_estimators=5, random_state=0)
regressor2.fit(X_train, Y_train)
Y_predict = regressor2.predict(X_test)
mse4 = MSE(Y_test, Y_predict)

x_grid = np.arange(min(X_train), max(X_train), 0.1).reshape(-1, 1)
plt.scatter(X_train, Y_train, color='blue')
plt.plot(x_grid, regressor2.predict(x_grid), color='red')
plt.title("Prédire les secteurs les plus préférables")
plt.xlabel('Les différents secteurs (encodés et normalisés)')
plt.ylabel('Les nombres de j\'aimes (normalisés)')
plt.show()

from sklearn.metrics import r2_score

# Prédiction et inverse de la transformation
r4= r2_score(Y_test, Y_predict)
print(f"MSE Linear Regression: {mse1}")
print(f"MSE SVR: {mse2}")
print(f"MSE Decision Tree: {mse3}")
print(f"MSE Random Forest: {mse4}")
x_encoded=x_encoded.reshape(1622,)
x_scaled=x_scaled.reshape(1622,)
y_scaled=y_scaled.reshape(1622,)

data={
      "Secteur":df1['Secteur'],
      "Secteur_encoded":x_encoded,
      "Secteur_ENCODED":x_scaled,
      "NB_JAIME":df1['NB_JAIME'],
      "NB_JAIME_ENODED":y_scaled
         }
output_path= r"C:\Users\21697\OneDrive\Bureau\lespepitestech_correspandancefinal.xlsx"
df88 = pd.DataFrame(data)
df88.to_excel(output_path)
