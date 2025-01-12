const fs = require('fs');
const path = require('path');
const readline = require('readline');

// Configuration pour lire les réponses de l'utilisateur dans le terminal
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout 
});

// Fonction pour extraire le préfixe du nom du fichier
function extrairePrefixe(fichier) {
    const correspondance = fichier.match(/^(\w{8})/); // Correspondance pour le format "SFIP96179"
    return correspondance ? correspondance[0] : fichier; // Retourne le préfixe ou le nom complet si aucune correspondance
}

// Fonction pour renommer les fichiers Excel dans un dossier donné
function traiterFichiersExcel(dossier, numeroDossier) {
    return new Promise((resolve) => {
        fs.readdir(dossier, (err, fichiers) => {
            if (err) {
                console.error("Erreur lors de la lecture du dossier :", err);
                resolve();
                return;
            }
         // Liste des préfixes autorisés
           const prefixes = ["SF", "9C", "LD", "HD", "TI","IS"];
            
            // Filtrer les fichiers pour ne garder que ceux avec les extensions .xls et .xlsx, et qui commencent par un préfixe autorisé
       let fichiersExcel = fichiers.filter(fichier => 
    (path.extname(fichier).toLowerCase() === '.xls' || path.extname(fichier).toLowerCase() === '.xlsx') &&
    prefixes.some(prefix => fichier.startsWith(prefix))
    );

            // Si des fichiers Excel sont trouvés, pose la question à l'utilisateur pour chaque fichier
            if (fichiersExcel.length > 0) {
                let index = 0;

                // Fonction récursive pour traiter chaque fichier un par un
                const traiterFichier = () => {
                    if (index < fichiersExcel.length) {
                        const fichier = fichiersExcel[index];
                        const prefixe = extrairePrefixe(fichier); // Extrait le préfixe
                        rl.question(`Y a-t-il une modification dans la fiche d'attribution pour le fichier ${prefixe} dans ${dossier}? (oui/non/spam) : `, (reponse) => {
                            const reponseUtilisateur = reponse.trim().toLowerCase(); // Normalise la réponse de l'utilisateur
                        
                            if (reponseUtilisateur === 'spam' || reponseUtilisateur === 's') {
                                // Si la réponse est "spam" ou "S", on passe au fichier suivant sans renommer
                                console.log(`Le fichier ${prefixe} est marqué comme spam. Il ne sera pas renommé. Passage au fichier suivant.`);
                                index++; // Passe au fichier suivant
                                traiterFichier(); // Traite le fichier suivant
                                return; // Ne fait rien d'autre pour ce fichier
                            }
                        
                            // Logique de renommage si la réponse est "oui" ou "non"
                            const nouveauNom = reponseUtilisateur === 'oui' ? 
                                `REC ${numeroDossier} NOK${path.extname(fichier)}` : 
                                `REC ${numeroDossier} OK${path.extname(fichier)}`;
                        
                            const cheminFichier = path.join(dossier, fichier);
                            const nouveauChemin = path.join(dossier, nouveauNom);
                        
                            // Renommage du fichier
                            fs.rename(cheminFichier, nouveauChemin, (err) => {
                                if (err) {
                                    console.error(`Erreur lors du renommage de ${fichier} :`, err);
                                } else {
                                    console.log(`${prefixe} renommé en ${nouveauNom.replace(path.extname(nouveauNom), '')} dans ${dossier}`);
                                }
                                index++; // Passe au fichier suivant
                                traiterFichier(); // Traite le fichier suivant
                            });
                        });
                        

                    } else {
                        // Une fois tous les fichiers traités, on résout la promesse
                        resolve();
                    }
                };

                traiterFichier(); // Démarre le traitement des fichiers
            } else {
                resolve(); // Résout la promesse si aucun fichier n'est trouvé
            }
        });
    });
}

// Fonction pour traiter les dossiers et les sous-dossiers
async function traiterDossiers(dossier) {
    try {
        const fichiers = await fs.promises.readdir(dossier);

        // Traiter le nom du dossier pour obtenir le numéro
        const dossierNom = path.basename(dossier);
        const numeroDossier = dossierNom.match(/^U\d{6}/) ? dossierNom : 'Inconnu'; // Assigne 'Inconnu' si le format n'est pas respecté

        console.log(`Traitement du dossier : ${dossier}`);

        // Traiter les fichiers Excel dans le dossier courant
        await traiterFichiersExcel(dossier, numeroDossier);

        // Traiter les sous-dossiers
        for (const fichier of fichiers) {
            const cheminFichier = path.join(dossier, fichier);
            const stats = await fs.promises.stat(cheminFichier).catch(err => {
                // Gérer l'erreur si le fichier ou dossier n'existe pas
                console.warn(`Le chemin ${cheminFichier} n'existe pas :`, err.message);
                return null; // Retourne null si le chemin n'existe pas
            });

            if (stats && stats.isDirectory()) {
                // Appel récursif pour traiter le sous-dossier seulement s'il existe
                await traiterDossiers(cheminFichier);
            }
        }
      
    } catch (err) {
        console.error(`Erreur lors du traitement du dossier ${dossier} :`, err);
    }
}

// Démarre le script en demandant à l'utilisateur d'entrer le chemin du dossier principal
rl.question('Entrez le chemin du répertoire principal : ', async (cheminDossierPrincipal) => {
    await traiterDossiers(cheminDossierPrincipal.trim());
    rl.close();
});
