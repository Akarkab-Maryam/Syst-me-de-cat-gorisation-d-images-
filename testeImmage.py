import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import pandas as pd

# Charger le modèle (chemin inchangé)
model_path = r"C:\Users\maryam\Documents\AutomRec\env\Lib\site-packages\modele_entraine.keras"
model = load_model(model_path)

# Afficher un résumé du modèle pour vérifier les dimensions
print("Résumé du modèle :")
model.summary()

# Demander à l'utilisateur de saisir le chemin du répertoire parent
dossier_parent = input("Entrez le chemin du répertoire parent contenant les dossiers d'images : ").strip()

# Vérifier si le répertoire parent existe
if not os.path.exists(dossier_parent):
    print("Le chemin spécifié n'existe pas. Veuillez vérifier.")
    exit()

# Parcourir tous les sous-dossiers dans le répertoire parent
for dossier_images in os.listdir(dossier_parent):
    chemin_dossier = os.path.join(dossier_parent, dossier_images)

    # Ignorer les fichiers ou chemins non répertoires
    if not os.path.isdir(chemin_dossier):
        print(f"Ignoré : {chemin_dossier} (non un dossier)")
        continue

    print(f"\nTraitement du dossier : {chemin_dossier}")

    # Extraire le numéro du dossier (si pertinent)
    numero_dossier = os.path.basename(chemin_dossier)

    # Dictionnaire pour regrouper les catégories par utilisateur
    resultats_utilisateur = {}

    # Parcourir les images dans le dossier
    for image_name in os.listdir(chemin_dossier):
        try:
            image_path = os.path.join(chemin_dossier, image_name)

            # Vérifier si le fichier est une image
            if not (image_name.endswith(".jpg") or image_name.endswith(".png") or image_name.endswith(".jpeg")):
                print(f"Fichier ignoré (non-image) : {image_name}")
                continue

            # Extraire le nom de l'utilisateur depuis le nom de fichier (avant le dernier '_')
            utilisateur = "_".join(image_name.split('_')[:-1])

            # Charger et redimensionner l'image à la taille utilisée lors de l'entraînement
            img = load_img(image_path, target_size=(150, 150))  # Remplacez 150x150 si une autre taille était utilisée
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)  # Ajouter une dimension pour le batch
            img_array = img_array / 255.0  # Normaliser les pixels (0-255 -> 0-1)

            # Prédiction
            prediction = model.predict(img_array)
            print(f"Forme de l'entrée pour {image_name} : {img_array.shape}")

            # Analyse des résultats
            categorie = np.argmax(prediction)  # Trouver la classe prédite
            if categorie == 0:
                categorie_nom = "RECOK"
            elif categorie == 1:
                categorie_nom = "RECNOK"
            else:
                categorie_nom = "Spam"

            # Ajouter la catégorie au dictionnaire pour l'utilisateur
            if utilisateur not in resultats_utilisateur:
                resultats_utilisateur[utilisateur] = []
            resultats_utilisateur[utilisateur].append((image_name, categorie_nom))

        except Exception as e:
            print(f"Erreur pour {image_name} : {e}")

    # Attribuer RECOK/RECNOK à une seule image, le reste devient Spam
    for utilisateur, images in resultats_utilisateur.items():
        has_rec = False  # Indique si RECOK ou RECNOK a été attribué
        for i, (image_name, categorie_nom) in enumerate(images):
            if not has_rec and categorie_nom in ["RECOK", "RECNOK"]:
                has_rec = True  # Garder cette image comme RECOK ou RECNOK
            else:
                # Toutes les autres images deviennent Spam
                images[i] = (image_name, "Spam")

    # Afficher un résumé des catégories par utilisateur
    print("\n=== Résumé par utilisateur ===")
    for utilisateur, images in resultats_utilisateur.items():
        print(f"Utilisateur : {utilisateur}")
        print(f" - Images analysées : {len(images)}")
        for image_name, categorie_nom in images:
            print(f"   - {image_name} : {categorie_nom}")

    # Parcourir les résultats pour ouvrir les images classifiées comme RECOK ou RECNOK
    for utilisateur, images in resultats_utilisateur.items():
        for image_name, categorie_nom in images:
            if categorie_nom in ["RECOK", "RECNOK"]:
                image_path = os.path.join(chemin_dossier, image_name)
                try:
                    print(f"Numéro du dossier : {numero_dossier}")
                    img = Image.open(image_path)
                    img.show()  # Ouvrir et afficher l'image
                    print(f"Image ouverte : {image_name} (Catégorie : {categorie_nom})")
                    input("Appuyez sur Entrée pour fermer l'image et continuer...")
                except Exception as e:
                    print(f"Erreur lors de l'ouverture de l'image {image_name} : {e}")
                    
# Liste pour stocker les résultats
resultats = []

# Initialiser un compteur pour le numéro du sous-dossier
num_sous_dossier = 1

# Parcourir tous les sous-dossiers dans le répertoire parent
for dossier_images in os.listdir(dossier_parent):
    chemin_dossier = os.path.join(dossier_parent, dossier_images)

    # Vérifier si c'est un dossier
    if not os.path.isdir(chemin_dossier):
        continue

    fichier_trouve = False  # Variable pour savoir si un fichier a été trouvé
    
    # Parcourir récursivement tous les sous-dossiers à l'intérieur
    for root, dirs, files in os.walk(chemin_dossier):  # Utilisation de os.walk pour parcourir récursivement
        for fichier in files:
            # Vérifier si le fichier est un fichier Excel et commence par "REC"
            if fichier.lower().startswith("rec") and (fichier.endswith(".xls") or fichier.endswith(".xlsx")):
                fichier_trouve = True
                break  # Si on trouve un fichier, on sort de la boucle

        if fichier_trouve:
            break  # On a trouvé un fichier, donc on arrête la recherche dans les sous-dossiers

    # Ajouter le résultat dans la liste avec le numéro du sous-dossier
    if not fichier_trouve:
        resultats.append([num_sous_dossier, chemin_dossier, "Aucun fichier trouvé"])
    else:
        resultats.append([num_sous_dossier, chemin_dossier, "Un fichier trouvé"])

    # Incrémenter le compteur de sous-dossier
    num_sous_dossier += 1

# Créer un DataFrame à partir des résultats
df = pd.DataFrame(resultats, columns=["Numéro du Sous-Dossier", "Dossier", "Résultat"])

# Afficher le tableau
print(df)
