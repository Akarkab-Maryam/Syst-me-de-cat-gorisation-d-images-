# Syst-me-de-cat-gorisation-d-images-

# Classificateur d'Images RECOK/RECNOK/Spam

Ce projet permet de classer des images en trois catégories : **RECOK**, **RECNOK**, et **Spam** en utilisant un modèle d'apprentissage profond entraîné avec Keras. Le modèle est utilisé pour prédire la catégorie des images, et les résultats sont affichés par utilisateur, avec les images correspondantes.

## Fonctionnalités de scripte python :

- Chargement et utilisation d'un modèle préalablement entraîné (`modele_entraine.keras`).
- Traitement d'un répertoire d'images et classification des images en trois catégories :
  - **RECOK** : Image reconnue comme étant valide.
  - **RECNOK** : Image reconnue comme étant non valide.
  - **Spam** : Image catégorisée comme spam.
- Ouverture des images classées comme **RECOK** ou **RECNOK** pour inspection.
- Parcours récursif des sous-dossiers à la recherche d'un fichier Excel, et affichage des résultats dans un tableau.
## Fonctionnalités de scripte  javascripte ( node js)

Le script est conçu pour renommer les fichiers Excel dans un dossier (et ses sous-dossiers) selon une logique définie et basée sur des interactions avec l'utilisateur. Voici les principales étapes et fonctionnalités :

1. Importation des modules nécessaires
fs : Fournit des fonctions pour manipuler le système de fichiers.
path : Aide à gérer les chemins de fichiers et dossiers.
readline : Permet d'interagir avec l'utilisateur via le terminal.


2. Extraction du préfixe
La fonction extrairePrefixe(fichier) extrait les 8 premiers caractères du nom de fichier qui suivent un certain format (par exemple, SFIP96179).
Si aucun préfixe valide n'est trouvé, le nom complet du fichier est retourné.


3. Filtrage et traitement des fichiers Excel
Les fichiers Excel sont identifiés par leurs extensions .xls ou .xlsx.
Seuls les fichiers dont le nom commence par un préfixe autorisé (SF, 9C, LD, HD, TI, IS) sont retenus.


4. Interaction avec l'utilisateur
Pour chaque fichier Excel :

Une question est posée à l'utilisateur pour savoir si une modification a été faite dans la fiche d'attribution.
Réponses possibles :
oui : Le fichier sera renommé avec le préfixe REC <NuméroDossier> NOK.
non : Le fichier sera renommé avec le préfixe REC <NuméroDossier> OK.
spam ou s : Le fichier est marqué comme "spam" et n'est pas renommé.



Fonctionnement du script :
Le script est conçu pour renommer les fichiers Excel dans un dossier (et ses sous-dossiers) selon une logique définie et basée sur des interactions avec l'utilisateur. Voici les principales étapes et fonctionnalités :

1. Importation des modules nécessaires
fs : Fournit des fonctions pour manipuler le système de fichiers.
path : Aide à gérer les chemins de fichiers et dossiers.
readline : Permet d'interagir avec l'utilisateur via le terminal.
2. Extraction du préfixe
La fonction extrairePrefixe(fichier) extrait les 8 premiers caractères du nom de fichier qui suivent un certain format (par exemple, SFIP96179).
Si aucun préfixe valide n'est trouvé, le nom complet du fichier est retourné.
3. Filtrage et traitement des fichiers Excel
Les fichiers Excel sont identifiés par leurs extensions .xls ou .xlsx.
Seuls les fichiers dont le nom commence par un préfixe autorisé (SF, 9C, LD, HD, TI, IS) sont retenus.
4. Interaction avec l'utilisateur
Pour chaque fichier Excel :

Une question est posée à l'utilisateur pour savoir si une modification a été faite dans la fiche d'attribution.
Réponses possibles :
oui : Le fichier sera renommé avec le préfixe REC <NuméroDossier> NOK.
non : Le fichier sera renommé avec le préfixe REC <NuméroDossier> OK.
spam ou s : Le fichier est marqué comme "spam" et n'est pas renommé.

5. Renommage des fichiers
Les fichiers sont renommés en utilisant fs.rename.
Les noms de fichiers sont formatés comme suit :
Si "oui" : REC <NuméroDossier> NOK.<extension>
Si "non" : REC <NuméroDossier> OK.<extension>


6. Traitement des sous-dossiers
Le script identifie les sous-dossiers grâce à fs.promises.stat et appelle la fonction traiterDossiers de manière récursive.


7. Structure principale
L'utilisateur fournit un chemin de répertoire principal.
Le script parcourt ce répertoire et traite tous les fichiers Excel et sous-dossiers en suivant la logique décrite.


Comportement en cas d'erreur
Les erreurs lors de la lecture des dossiers ou fichiers sont capturées et affichées dans la console.
Si un chemin n'existe pas, une alerte est affichée, et le traitement continue.




## Prérequis

Avant de commencer, assurez-vous d'avoir installé les bibliothèques nécessaires. Vous pouvez installer les dépendances avec le fichier `requirements.txt` (voir ci-dessous pour plus de détails).

### Bibliothèques nécessaires  python :

- `tensorflow` : Pour utiliser le modèle Keras.
- `numpy` : Pour les manipulations de données.
- `PIL` (Python Imaging Library) : Pour ouvrir et afficher les images.
- `pandas` : Pour gérer les résultats dans un tableau.

### Bibliothèques nécessaires node js  :
1. Node.js
Le script utilise Node.js, donc vous devez installer Node.js sur votre machine.
Téléchargez-le depuis le site officiel de Node.js.
2. Modules intégrés de Node.js
Les modules utilisés dans ce script (fs, path, readline) sont intégrés dans Node.js. Vous n'avez pas besoin de les installer séparément.
3. Packages additionnels
Aucun package externe n'est requis pour ce script.
4. Étapes pour tester et exécuter le script
Vérifiez que Node.js est installé :

bash
Copier le code
node -v
Cela doit afficher une version (par exemple, v16.x.x ou v18.x.x).

Créez un fichier pour votre script :

Enregistrez le code dans un fichier nommé renommer_fichiers.js dans un répertoire de votre choix.
Exécutez le script :

Dans un terminal ou une invite de commande, exécutez la commande suivante :
bash
Copier le code
node renommer_fichiers.js
5. Chemin du dossier principal
Lorsque le script vous demande d'entrer le chemin du répertoire principal, assurez-vous de spécifier un chemin valide, comme :
bash
Copier le code
D:\TImage\Documents
