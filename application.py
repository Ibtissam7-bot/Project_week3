# app.py
import streamlit as st
import pandas as pd
import joblib

# Charger le modèle et les colonnes
model = joblib.load("random_forest_model.pkl")
columns = list(model.feature_names_in_)

st.title("🧮 Estimation du prix d'un appartement")

# Collecter les inputs utilisateur
surface = st.number_input("Surface en m²", min_value=20, max_value=500, value=100)
nb_rooms = st.number_input("Nombre de chambres", min_value=1, max_value=10, value=3)
salon = st.number_input("Nombre de salons", min_value=0, max_value=5, value=1)
#baths = st.number_input("Nombre de salles de bain", min_value=1, max_value=5, value=2)
ascenseur = st.checkbox("Ascenseur")
parking = st.checkbox("Parking")
#chauffage = st.checkbox("Chauffage")
terrasse = st.checkbox("Terrasse")
clim = st.checkbox("Climatisation")

# Construire nb_total_pieces
nb_total_pieces = nb_rooms + salon

# Créer input
input_data = pd.DataFrame([{
    'surface_area': surface,
    'nb_rooms': nb_rooms,
    # 'salon': salon,
    # 'nb_baths': baths,
    'Ascenseur': int(ascenseur),
    'Parking': int(parking),
    # 'Chauffage': int(chauffage),
    'Terrasse': int(terrasse),
    'Climatisation': int(clim),
    'nb_total_pieces': nb_total_pieces
}])

# Ajouter colonnes manquantes
for col in columns:
    if col not in input_data.columns:
        input_data[col] = 0

# Réordonner
input_data = input_data[columns]

# Prédire
if st.button("Prédire le prix"):
    prediction = model.predict(input_data)[0]
    st.success(f"🏠 Prix estimé : {prediction:,.0f} MAD")
