# SalesHouses – Simulateur intelligent d'évaluation immobilière

## Objectif du projet

Ce projet s’inscrit dans le cadre d’une mission confiée par la société SalesHouses, plateforme marocaine spécialisée dans les transactions immobilières. 
L’objectif est de développer un **simulateur d’évaluation de prix immobilier**, basé sur l’intelligence artificielle,
afin de fournir aux utilisateurs une estimation fiable du prix de leur bien à partir de ses caractéristiques.

## Modalité de réalisation
 Durée : 5 jours (du 14 au 18 juillet 2025)

## Projet individuel

 Contexte pédagogique encadré par simplon academy
 
 **Suivi en mode agile (Jira + Kanban)**
 Veuillez consultez votre boite mail pour accéder à ma planification sur Jira.

## Autrice

Nom : Ibtissam Sannaky

Contact : bissamsannaky@gmail.com

## Méthodologie

Le projet suit une démarche rigoureuse en plusieurs étapes :

1. **Chargement et exploration des données** (`pandas`)
2. **Analyse exploratoire (EDA)** : compréhension de la structure, visualisations, corrélations
3. **Nettoyage et prétraitement** :
   - Conversion de la variable `price` en float
   - Encodage des équipements (get_dummies)
   - Traitement de la colonne `city_name`
   - Gestion des valeurs manquantes
   - Suppression des outliers (Boites à moustaches)
   - ...
4. **Sélection des variables explicatives** : basées sur la corrélation avec la cible
5. **Mise à l’échelle des variables numériques** (StandardScaler)
6. **Entraînement de plusieurs modèles supervisés** :
   - Régression linéaire
   - Random Forest Regressor
   - SVR (Support Vector Regressor)
   - Gradient Boosting Regressor
7. **Évaluation des performances** :
   - Métriques utilisées : R², RMSE, MAE, MSE
   - Validation croisée (`cross_val_score`)
8. **Optimisation des hyperparamètres** (`GridSearchCV`)
9. **Sauvegarde du meilleur modèle** (`joblib`)
10. **Déploiement d'une interface utilisateur avec Streamlit**

## Résultats

- **Modèle retenu** : Gradient Boosting Regresor
- **Score R² obtenu** : 0.40 (sur des données bruitées)
- **Justification** : modèle robuste face aux valeurs extrêmes, meilleure capacité à modéliser les non-linéarités

## Exemple de prédiction
Un appartement à Casablanca, 70m², 3 chambres, 1 salon, 2 SDB, avec Ascenseur et Climatisation →
 **Prix estimé par le modèle** :  704,165.60 MAD (valeur réaliste)


##  Application Streamlit

L’utilisateur peut accéder à une application interactive qui lui permet de :
- Saisir les caractéristiques du bien (surface, nb pièces, équipements, etc.)
- Obtenir instantanément une estimation du prix

Pour lancer l'application localement :

```bash
pip install -r requirements.txt
streamlit run app.py
```
## Contenus de chaque fichier
**appartements-data-db-6872f0ba853ec096170787.csv** : Contient le jeux de données correspondant sous format .csv.

**Source_file.ipynb** : Contient le code source du projet.

**Gradient_boosting.pkl**: Sauvegarder le modèle entraîné  Gradient boosting.

**random_forest_model.pkl**:Sauvegarder le modèle entraîné Random Forest.

**Test.ipynb**: Fichier Python pour tester le modèle choisi.

**application.py**: Contient le code permettant de lancer l'application Streamlit localement.

