import os
import shutil

# Dossier source où les fichiers sont actuellement
source_folder = "/chemin/vers/ton/dossier"

# Dossiers de destination
image_folder = "/chemin/vers/ton/dossier/images"
document_folder = "/chemin/vers/ton/dossier/documents"
other_folder = "/chemin/vers/ton/dossier/autres"

# Liste des extensions pour chaque type de fichier
image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
document_extensions = ['.pdf', '.txt', '.docx', '.xlsx']

def organiser_fichiers():
    for fichier in os.listdir(source_folder):
        chemin_complet = os.path.join(source_folder, fichier)
        
        if os.path.isfile(chemin_complet):
            # Obtenir l'extension du fichier
            ext = os.path.splitext(fichier)[1].lower()
            
            if ext in image_extensions:
                destination = image_folder
            elif ext in document_extensions:
                destination = document_folder
            else:
                destination = other_folder
            
            # Déplacer le fichier vers le bon dossier
            shutil.move(chemin_complet, os.path.join(destination, fichier))
            print(f"Le fichier {fichier} a été déplacé vers {destination}")

if __name__ == "__main__":
    organiser_fichiers()
