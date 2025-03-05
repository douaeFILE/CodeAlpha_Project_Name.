import random
import nltk
from nltk.corpus import words

# Télécharger la liste des mots si ce n'est pas déjà fait
nltk.download('words')

# Récupérer tous les mots anglais
liste_mots = words.words()

# Choisir un mot aléatoire
o = random.choice(liste_mots).lower()  # Mot à deviner en minuscule

# Nombre d'erreurs maximum
nerr = 6

# Demander une lettre à l'utilisateur
u = input("Devinez une lettre du mot anglais : ").lower()

while nerr > 0:
    trouve = False  # Variable pour vérifier si la lettre est trouvée

    for i in range(len(o)):
        if u == o[i]:
            print(f"Bravo ! Vous avez deviné la lettre '{u}'.")
            trouve = True
            break  # Sortir de la boucle car la lettre est trouvée

    if not trouve:
        print("Mauvaise réponse, essayez encore.")
        nerr -= 1
        print(f"Il vous reste {nerr} essais.")

    if nerr > 0:  # Ne redemander que si l'utilisateur a encore des essais
        u = input("Devinez une autre lettre du mot anglais : ").lower()

print(f"Le mot était : {o}")
