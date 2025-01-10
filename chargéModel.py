# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:21:49 2024

@author: maryam
"""

import tensorflow as tf

# Spécifiez le chemin vers votre fichier .keras
model_path = r"C:\Users\maryam\Documents\AutomRec\env\Lib\site-packages\modele_entraine.keras"

# Charger le modèle
try:
    model = tf.keras.models.load_model(model_path)
    print("Modèle chargé avec succès !")
    
    # Afficher un résumé du modèle
    model.summary()
except Exception as e:
    print(f"Erreur lors du chargement du modèle : {e}")
