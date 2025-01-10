# Syst-me-de-cat-gorisation-d-images-

# Classificateur d'Images RECOK/RECNOK/Spam

Ce projet permet de classer des images en trois catégories : **RECOK**, **RECNOK**, et **Spam** en utilisant un modèle d'apprentissage profond entraîné avec Keras. Le modèle est utilisé pour prédire la catégorie des images, et les résultats sont affichés par utilisateur, avec les images correspondantes.

## Fonctionnalités

- Chargement et utilisation d'un modèle préalablement entraîné (`modele_entraine.keras`).
- Traitement d'un répertoire d'images et classification des images en trois catégories :
  - **RECOK** : Image reconnue comme étant valide.
  - **RECNOK** : Image reconnue comme étant non valide.
  - **Spam** : Image catégorisée comme spam.
- Ouverture des images classées comme **RECOK** ou **RECNOK** pour inspection.
- Parcours récursif des sous-dossiers à la recherche d'un fichier Excel, et affichage des résultats dans un tableau.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les bibliothèques nécessaires. Vous pouvez installer les dépendances avec le fichier `requirements.txt` (voir ci-dessous pour plus de détails).

### Bibliothèques nécessaires

- `tensorflow` : Pour utiliser le modèle Keras.
- `numpy` : Pour les manipulations de données.
- `PIL` (Python Imaging Library) : Pour ouvrir et afficher les images.
- `pandas` : Pour gérer les résultats dans un tableau.


